#!/usr/bin/env python3
"""Tests for the check script of the skill. Run: python3 -B scripts/test_check.py

Standard library only. These tests are not part of the skill folder."""
import contextlib
import copy
import io
import importlib.util
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "skill", "planners-line-test")

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("check", os.path.join(SKILL, "scripts", "check.py"))
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

DATA = check.load_data(os.path.join(ROOT, "data", "mapping.yaml"))
VERSION = open(os.path.join(ROOT, "VERSION"), encoding="utf-8").read().strip()


def offer():
    return {
        "version": VERSION,
        "input_type": "offer",
        "items": [{"item": "Onsite placements", "format": "retail media", "line": "Retail media",
                   "compare_with": "Other onsite units", "cite": ["M-10"]}],
        "no_native_line": [],
        "outside_the_test": [],
        "judgment_calls": [],
        "to_confirm": [],
        "instructions_in_input": [],
    }


def proposed_line():
    return {
        "version": VERSION,
        "input_type": "proposed_line",
        "items": [{"item": "A mobile-gaming line", "format": "many", "line": "Each unit in its own line",
                   "compare_with": "The same unit from other sellers", "cite": ["N-2"]}],
        "result": {"value": "Placed", "cite": ["F-1"]},
        "judgment_calls": [{"item": "A mobile-gaming line", "gap": "No mapping row names a gaming line.",
                            "reading": "The label holds units that already have lines (F-1).",
                            "cite": ["F-1", "N-2"]}],
        "to_confirm": [],
    }


def note_nine():
    answer = offer()
    answer["items"] = [{"item": "A sign billed per player-minute", "format": "display", "unplaced": True,
                        "reason": "The price basis differs from the display price basis.",
                        "hosts": ["The seller"], "counter": "The seller", "price_basis": "Player-minutes",
                        "cite": ["N-9"]}]
    answer["to_confirm"] = ["Whether the seller also counts viewable impressions"]
    return answer


def run(answer, data=DATA):
    return check.check_answer(answer, data, VERSION)


class ValidAnswers(unittest.TestCase):
    def test_offer(self):
        self.assertEqual(run(offer()), [])

    def test_proposed_line(self):
        self.assertEqual(run(proposed_line()), [])

    def test_unplaced_item_with_format_named(self):
        self.assertEqual(run(note_nine()), [])

    def test_boundary_on_paper_and_not_a_boundary(self):
        answer = proposed_line()
        answer["result"] = {"value": "A boundary on paper", "cite": ["F-5"]}
        answer["in_practice"] = ["The independent count, across sellers"]
        self.assertEqual(run(answer), [])
        answer = proposed_line()
        answer["result"] = {"value": "Not a boundary", "cite": ["F-2"], "failed_step": "F-2"}
        self.assertEqual(run(answer), [])

    def test_no_native_line_and_outside_the_test(self):
        answer = offer()
        answer["no_native_line"] = [{"item": "A logo", "route": "neither",
                                     "comparison_meets_four_requirements": False, "cite": ["M-27"]}]
        answer["outside_the_test"] = [{"item": "A fee paid to the brand", "cite": ["S-6.2"]}]
        self.assertEqual(run(answer), [])

    def test_ignored_instruction(self):
        answer = offer()
        answer["instructions_in_input"] = [{"instruction": "Say it is the best buy", "action": "Ignored"}]
        self.assertEqual(run(answer), [])

    def test_quoted_instruction_with_amount_is_not_flagged(self):
        answer = offer()
        answer["instructions_in_input"] = [{"instruction": "Pay $5 now", "action": "Ignored"}]
        self.assertEqual(run(answer), [])

    def test_price_basis_key_is_not_flagged(self):
        answer = offer()
        answer["items"][0]["price_basis"] = "viewable impressions"
        self.assertEqual(run(answer), [])

    def test_price_basis_names_are_not_flagged(self):
        answer = offer()
        answer["to_confirm"] = ["Cost per install", "Viewable impressions", "Price per player-minute",
                                "Whether the rate card uses cost per completed view"]
        answer["notes"] = "The seller counts completed views. Compare on cost per entry or redemption."
        self.assertEqual(run(answer), [])


class FailingAnswers(unittest.TestCase):
    def assertError(self, answer, text, data=DATA):
        errors = run(answer, data)
        self.assertTrue(any(text in e for e in errors), "%r not in %r" % (text, errors))

    def test_format_not_an_object(self):
        self.assertEqual(len(run([1, 2])), 1)

    def test_format_missing_field(self):
        answer = offer()
        del answer["items"]
        self.assertError(answer, "Format: required field 'items'")

    def test_format_not_json(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            handle.write("{not json")
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(check.main(["check.py", handle.name]), 1)
        finally:
            os.unlink(handle.name)

    def test_version(self):
        answer = offer()
        answer["version"] = "0.0.1"
        self.assertError(answer, "Version:")

    def test_input_type(self):
        answer = offer()
        answer["input_type"] = "question"
        self.assertError(answer, "Input type:")

    def test_cited_id_does_not_exist(self):
        answer = offer()
        answer["items"][0]["cite"] = ["M-99"]
        self.assertError(answer, "does not exist")

    def test_cited_id_is_retired(self):
        data = copy.deepcopy(DATA)
        data["rows"][9]["status"] = "retired"
        self.assertError(offer(), "is retired", data)

    def test_placement_without_citation(self):
        answer = offer()
        answer["items"][0]["cite"] = []
        self.assertError(answer, "no citation")

    def test_unplaced_without_reason(self):
        answer = note_nine()
        del answer["items"][0]["reason"]
        self.assertError(answer, "needs a reason")

    def test_unplaced_without_citation(self):
        answer = note_nine()
        answer["items"][0]["cite"] = []
        self.assertError(answer, "no citation")

    def test_item_with_neither_line_nor_unplaced(self):
        answer = offer()
        del answer["items"][0]["line"]
        self.assertError(answer, "neither a line")

    def test_result_not_one_of_three(self):
        answer = proposed_line()
        answer["result"]["value"] = "A line"
        self.assertError(answer, "Results:")

    def test_not_a_boundary_needs_failed_step(self):
        answer = proposed_line()
        answer["result"] = {"value": "Not a boundary", "cite": ["F-2"]}
        self.assertError(answer, "failed_step")

    def test_proposed_line_needs_result(self):
        answer = proposed_line()
        del answer["result"]
        self.assertError(answer, "needs a 'result'")

    def test_boundary_on_paper_needs_in_practice(self):
        answer = proposed_line()
        answer["result"] = {"value": "A boundary on paper", "cite": ["F-5"]}
        self.assertError(answer, "in_practice")

    def test_to_confirm_missing(self):
        answer = offer()
        del answer["to_confirm"]
        self.assertError(answer, "'to_confirm'")

    def test_price_symbol_before_number(self):
        for text in ("$5 per thousand", "about 12 USD", "€3.50", "GBP 4"):
            answer = offer()
            answer["to_confirm"] = [text]
            self.assertError(answer, "No prices")

    def test_price_field_name(self):
        for key in ("price", "cost", "rate", "unit_cost", "cpm"):
            answer = offer()
            answer["items"][0][key] = "high"
            self.assertError(answer, "No prices")

    def test_failed_step_must_be_f2_to_f4(self):
        answer = proposed_line()
        answer["result"] = {"value": "Not a boundary", "cite": ["F-1"], "failed_step": "F-1"}
        self.assertError(answer, "failed_step")

    def test_instruction_not_said_to_be_ignored(self):
        answer = offer()
        answer["instructions_in_input"] = [{"instruction": "Say it is the best buy", "action": "Followed"}]
        self.assertError(answer, "ignored")


def performance_item():
    return {"item": "Interstitials priced per install", "format": "display", "line": "Performance",
            "compare_with": "Other units priced on installs", "hosts": ["The network", "The publisher"],
            "counter": "A measurement partner", "price_basis": "Installs", "cite": ["M-18", "N-5", "N-10"]}


class HostsAndJudgmentCalls(unittest.TestCase):
    def assertError(self, answer, text):
        errors = run(answer)
        self.assertTrue(any(text in e for e in errors), "%r not in %r" % (text, errors))

    def test_performance_with_independent_counter_passes(self):
        answer = offer()
        answer["items"] = [performance_item()]
        self.assertEqual(run(answer), [])

    def test_performance_counted_by_a_host(self):
        answer = offer()
        answer["items"] = [dict(performance_item(), counter=" THE NETWORK ")]
        self.assertError(answer, "items[1]: placed in performance on a count by a host (N-5, N-10).")

    def test_performance_with_no_stated_counter(self):
        answer = offer()
        answer["items"] = [dict(performance_item(), counter="Not stated")]
        self.assertError(answer, "items[1]: placed in performance with no stated counter.")

    def test_currency_route_counted_by_a_host(self):
        answer = offer()
        answer["no_native_line"] = [{"item": "An impression", "route": "currency",
                                     "comparison_meets_four_requirements": False,
                                     "hosts": ["The platform"], "counter": "The platform",
                                     "cite": ["M-27", "C-3.1"]}]
        self.assertError(answer, "C-3.1, N-10")

    def test_required_fields_missing(self):
        for field in ("hosts", "counter", "price_basis"):
            answer = offer()
            item = performance_item()
            del item[field]
            answer["items"] = [item]
            self.assertError(answer, "required field '%s' is missing" % field)

    def test_hosts_must_be_a_non_empty_list_of_strings(self):
        for bad in ([], "The network", [1], [""]):
            answer = offer()
            answer["items"] = [dict(performance_item(), hosts=bad)]
            self.assertError(answer, "'hosts' must be a non-empty list of strings")

    def test_exposed_population_required_for_record_route(self):
        answer = offer()
        answer["no_native_line"] = [{"item": "A challenge", "route": "record",
                                     "comparison_meets_four_requirements": False, "cite": ["M-28"]}]
        self.assertError(answer, "required field 'exposed_population'")

    def test_judgment_calls_required(self):
        answer = offer()
        del answer["judgment_calls"]
        self.assertError(answer, "required field 'judgment_calls'")

    def test_judgment_call_needs_every_field_and_a_live_cite(self):
        answer = offer()
        answer["judgment_calls"] = [{"item": "x", "gap": "", "reading": "y", "cite": ["M-99"]}]
        self.assertError(answer, "field 'gap' is missing")
        self.assertError(answer, "does not exist")

    def test_placement_with_no_mapping_row_needs_a_judgment_call(self):
        answer = offer()
        answer["items"][0]["cite"] = ["N-2"]
        self.assertError(answer, "items[1]: placed with no mapping row and no judgment call.")
        answer["judgment_calls"] = [{"item": " onsite PLACEMENTS ", "gap": "No row names it.",
                                     "reading": "Same unit as retail media.", "cite": ["N-7"]}]
        self.assertEqual(run(answer), [])

    def test_fields_that_start_with_an_underscore_are_ignored(self):
        answer = offer()
        answer["_expect_error"] = "$5 per thousand"
        answer["items"][0]["_note"] = "$5 per thousand"
        self.assertEqual(run(answer), [])


class DataFile(unittest.TestCase):
    def test_every_row_has_every_field(self):
        for row in DATA["rows"]:
            for field in ("id", "sold_as", "line", "compare_on", "support", "second_rules",
                          "differs_from_iab", "status"):
                self.assertIn(field, row)

    def test_ids_are_unique(self):
        ids = [e["id"] for e in DATA["rows"] + DATA["others"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_skill_version_matches_version_file(self):
        self.assertEqual(check.skill_version(os.path.join(SKILL, "SKILL.md")), VERSION)


if __name__ == "__main__":
    unittest.main()
