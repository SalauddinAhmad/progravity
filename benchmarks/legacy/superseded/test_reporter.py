from repair_runner_v2 import check_contamination, dump_manifest

# Contamination tests
def test_contamination():
    # Baseline
    m_baseline = {"mode": "BASELINE", "skills": {}, "config_plugins": {"progravity": {"enabled": False}}}
    check_contamination(m_baseline, "BASELINE") # should pass
    try:
        check_contamination({"mode": "BASELINE", "skills": {"progravity": "exists"}, "config_plugins": {}}, "BASELINE")
        assert False, "Should have failed"
    except AssertionError:
        pass

    # Core
    m_core = {"mode": "PROGRAVITY_CORE", "skills": {"progravity": "exists"}, "config_plugins": {"progravity": {"enabled": False}}}
    check_contamination(m_core, "PROGRAVITY_CORE") # should pass
    
    # Native
    m_native = {"mode": "PROGRAVITY_NATIVE", "skills": {"progravity": "exists"}, "config_plugins": {"progravity": {"enabled": True}}}
    check_contamination(m_native, "PROGRAVITY_NATIVE") # should pass

test_contamination()
print("REPORTER TESTS PASSED")
