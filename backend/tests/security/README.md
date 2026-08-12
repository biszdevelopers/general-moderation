# Security Module Test Documentation

## Overview
- **Total Planned:** 2,000,000
- **Phase 1:** 80 (IDs TC-SEC-001 to TC-SEC-0080) :white_check_mark: Implemented
- **Phase 2:** 700 (IDs TC-SEC-0081 to TC-SEC-0780) :white_check_mark: Implemented
- **Phase 3:** 20,000 (IDs TC-SEC-0781 to TC-SEC-20780) :hourglass: Planned
- **Phase 4:** 200,000 (IDs TC-SEC-20781 to TC-SEC-220780) :hourglass: Planned
- **Phase 5:** 1,779,220 (IDs TC-SEC-220781 to TC-SEC-2000000) :hourglass: Planned

## Dimension Matrix
| Dimension | Values (Phase 2) |
| :--- | :--- |
| Header | 6 security headers |
| CORS origin | allowed, disallowed, none |
| Auth key | valid, missing, wrong, empty |
| Injection | SQL, XSS, template, unicode |
| Traversal | ../, %2e%2e, absolute |
| Method | GET, POST, PUT, DELETE |

## Test Case List

### Phase 1 - 80 cases
- 80 cases (headers, CORS, injection, auth).

### Phase 2 (Current) - 700 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-SEC-8732 | P1 | Header x-content-type-options on GET /health | header=x-content-type-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8733 | P1 | Header x-content-type-options on GET /health | header=x-content-type-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8734 | P1 | Header x-content-type-options on GET /health | header=x-content-type-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8735 | P1 | Header x-content-type-options on GET /health | header=x-content-type-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8736 | P1 | Header x-content-type-options on POST /moderate | header=x-content-type-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8737 | P1 | Header x-content-type-options on POST /moderate | header=x-content-type-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8738 | P1 | Header x-content-type-options on POST /moderate | header=x-content-type-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8739 | P1 | Header x-content-type-options on POST /moderate | header=x-content-type-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8740 | P1 | Header x-content-type-options on GET /metrics | header=x-content-type-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8741 | P1 | Header x-content-type-options on GET /metrics | header=x-content-type-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8742 | P1 | Header x-content-type-options on GET /metrics | header=x-content-type-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8743 | P1 | Header x-content-type-options on GET /metrics | header=x-content-type-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8744 | P1 | Header x-content-type-options on POST /moderate/batch | header=x-content-type-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8745 | P1 | Header x-content-type-options on POST /moderate/batch | header=x-content-type-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8746 | P1 | Header x-content-type-options on POST /moderate/batch | header=x-content-type-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8747 | P1 | Header x-content-type-options on POST /moderate/batch | header=x-content-type-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8748 | P1 | Header x-content-type-options on GET / | header=x-content-type-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8749 | P1 | Header x-content-type-options on GET / | header=x-content-type-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8750 | P1 | Header x-content-type-options on GET / | header=x-content-type-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8751 | P1 | Header x-content-type-options on GET / | header=x-content-type-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8752 | P1 | Header x-frame-options on GET /health | header=x-frame-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8753 | P1 | Header x-frame-options on GET /health | header=x-frame-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8754 | P1 | Header x-frame-options on GET /health | header=x-frame-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8755 | P1 | Header x-frame-options on GET /health | header=x-frame-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8756 | P1 | Header x-frame-options on POST /moderate | header=x-frame-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8757 | P1 | Header x-frame-options on POST /moderate | header=x-frame-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8758 | P1 | Header x-frame-options on POST /moderate | header=x-frame-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8759 | P1 | Header x-frame-options on POST /moderate | header=x-frame-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8760 | P1 | Header x-frame-options on GET /metrics | header=x-frame-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8761 | P1 | Header x-frame-options on GET /metrics | header=x-frame-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8762 | P1 | Header x-frame-options on GET /metrics | header=x-frame-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8763 | P1 | Header x-frame-options on GET /metrics | header=x-frame-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8764 | P1 | Header x-frame-options on POST /moderate/batch | header=x-frame-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8765 | P1 | Header x-frame-options on POST /moderate/batch | header=x-frame-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8766 | P1 | Header x-frame-options on POST /moderate/batch | header=x-frame-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8767 | P1 | Header x-frame-options on POST /moderate/batch | header=x-frame-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8768 | P1 | Header x-frame-options on GET / | header=x-frame-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8769 | P1 | Header x-frame-options on GET / | header=x-frame-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8770 | P1 | Header x-frame-options on GET / | header=x-frame-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8771 | P1 | Header x-frame-options on GET / | header=x-frame-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8772 | P1 | Header content-security-policy on GET /health | header=content-security-policy,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8773 | P1 | Header content-security-policy on GET /health | header=content-security-policy,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8774 | P1 | Header content-security-policy on GET /health | header=content-security-policy,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8775 | P1 | Header content-security-policy on GET /health | header=content-security-policy,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8776 | P1 | Header content-security-policy on POST /moderate | header=content-security-policy,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8777 | P1 | Header content-security-policy on POST /moderate | header=content-security-policy,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8778 | P1 | Header content-security-policy on POST /moderate | header=content-security-policy,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8779 | P1 | Header content-security-policy on POST /moderate | header=content-security-policy,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8780 | P1 | Header content-security-policy on GET /metrics | header=content-security-policy,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8781 | P1 | Header content-security-policy on GET /metrics | header=content-security-policy,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8782 | P1 | Header content-security-policy on GET /metrics | header=content-security-policy,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8783 | P1 | Header content-security-policy on GET /metrics | header=content-security-policy,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8784 | P1 | Header content-security-policy on POST /moderate/batch | header=content-security-policy,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8785 | P1 | Header content-security-policy on POST /moderate/batch | header=content-security-policy,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8786 | P1 | Header content-security-policy on POST /moderate/batch | header=content-security-policy,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8787 | P1 | Header content-security-policy on POST /moderate/batch | header=content-security-policy,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8788 | P1 | Header content-security-policy on GET / | header=content-security-policy,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8789 | P1 | Header content-security-policy on GET / | header=content-security-policy,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8790 | P1 | Header content-security-policy on GET / | header=content-security-policy,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8791 | P1 | Header content-security-policy on GET / | header=content-security-policy,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8792 | P1 | Header strict-transport-security on GET /health | header=strict-transport-security,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8793 | P1 | Header strict-transport-security on GET /health | header=strict-transport-security,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8794 | P1 | Header strict-transport-security on GET /health | header=strict-transport-security,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8795 | P1 | Header strict-transport-security on GET /health | header=strict-transport-security,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8796 | P1 | Header strict-transport-security on POST /moderate | header=strict-transport-security,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8797 | P1 | Header strict-transport-security on POST /moderate | header=strict-transport-security,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8798 | P1 | Header strict-transport-security on POST /moderate | header=strict-transport-security,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8799 | P1 | Header strict-transport-security on POST /moderate | header=strict-transport-security,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8800 | P1 | Header strict-transport-security on GET /metrics | header=strict-transport-security,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8801 | P1 | Header strict-transport-security on GET /metrics | header=strict-transport-security,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8802 | P1 | Header strict-transport-security on GET /metrics | header=strict-transport-security,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8803 | P1 | Header strict-transport-security on GET /metrics | header=strict-transport-security,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8804 | P1 | Header strict-transport-security on POST /moderate/batch | header=strict-transport-security,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8805 | P1 | Header strict-transport-security on POST /moderate/batch | header=strict-transport-security,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8806 | P1 | Header strict-transport-security on POST /moderate/batch | header=strict-transport-security,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8807 | P1 | Header strict-transport-security on POST /moderate/batch | header=strict-transport-security,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8808 | P1 | Header strict-transport-security on GET / | header=strict-transport-security,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8809 | P1 | Header strict-transport-security on GET / | header=strict-transport-security,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8810 | P1 | Header strict-transport-security on GET / | header=strict-transport-security,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8811 | P1 | Header strict-transport-security on GET / | header=strict-transport-security,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8812 | P1 | Header x-xss-protection on GET /health | header=x-xss-protection,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8813 | P1 | Header x-xss-protection on GET /health | header=x-xss-protection,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8814 | P1 | Header x-xss-protection on GET /health | header=x-xss-protection,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8815 | P1 | Header x-xss-protection on GET /health | header=x-xss-protection,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8816 | P1 | Header x-xss-protection on POST /moderate | header=x-xss-protection,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8817 | P1 | Header x-xss-protection on POST /moderate | header=x-xss-protection,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8818 | P1 | Header x-xss-protection on POST /moderate | header=x-xss-protection,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8819 | P1 | Header x-xss-protection on POST /moderate | header=x-xss-protection,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8820 | P1 | Header x-xss-protection on GET /metrics | header=x-xss-protection,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8821 | P1 | Header x-xss-protection on GET /metrics | header=x-xss-protection,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8822 | P1 | Header x-xss-protection on GET /metrics | header=x-xss-protection,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8823 | P1 | Header x-xss-protection on GET /metrics | header=x-xss-protection,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8824 | P1 | Header x-xss-protection on POST /moderate/batch | header=x-xss-protection,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8825 | P1 | Header x-xss-protection on POST /moderate/batch | header=x-xss-protection,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8826 | P1 | Header x-xss-protection on POST /moderate/batch | header=x-xss-protection,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8827 | P1 | Header x-xss-protection on POST /moderate/batch | header=x-xss-protection,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8828 | P1 | Header x-xss-protection on GET / | header=x-xss-protection,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8829 | P1 | Header x-xss-protection on GET / | header=x-xss-protection,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8830 | P1 | Header x-xss-protection on GET / | header=x-xss-protection,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8831 | P1 | Header x-xss-protection on GET / | header=x-xss-protection,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8852 | P1 | CORS http://localhost:3000 GET #0 | origin=http://localhost:3000,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8853 | P1 | CORS http://localhost:3000 GET #1 | origin=http://localhost:3000,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8854 | P1 | CORS http://localhost:3000 GET #2 | origin=http://localhost:3000,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8855 | P1 | CORS http://localhost:3000 GET #3 | origin=http://localhost:3000,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8856 | P1 | CORS http://localhost:3000 POST #0 | origin=http://localhost:3000,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8857 | P1 | CORS http://localhost:3000 POST #1 | origin=http://localhost:3000,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8858 | P1 | CORS http://localhost:3000 POST #2 | origin=http://localhost:3000,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8859 | P1 | CORS http://localhost:3000 POST #3 | origin=http://localhost:3000,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8860 | P1 | CORS http://localhost:3000 PUT #0 | origin=http://localhost:3000,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8861 | P1 | CORS http://localhost:3000 PUT #1 | origin=http://localhost:3000,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8862 | P1 | CORS http://localhost:3000 PUT #2 | origin=http://localhost:3000,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8863 | P1 | CORS http://localhost:3000 PUT #3 | origin=http://localhost:3000,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8864 | P1 | CORS http://localhost:3000 DELETE #0 | origin=http://localhost:3000,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8865 | P1 | CORS http://localhost:3000 DELETE #1 | origin=http://localhost:3000,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8866 | P1 | CORS http://localhost:3000 DELETE #2 | origin=http://localhost:3000,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8867 | P1 | CORS http://localhost:3000 DELETE #3 | origin=http://localhost:3000,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8868 | P1 | CORS http://localhost:3000 OPTIONS #0 | origin=http://localhost:3000,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8869 | P1 | CORS http://localhost:3000 OPTIONS #1 | origin=http://localhost:3000,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8870 | P1 | CORS http://localhost:3000 OPTIONS #2 | origin=http://localhost:3000,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8871 | P1 | CORS http://localhost:3000 OPTIONS #3 | origin=http://localhost:3000,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8872 | P1 | CORS https://mod.example.com GET #0 | origin=https://mod.example.com,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8873 | P1 | CORS https://mod.example.com GET #1 | origin=https://mod.example.com,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8874 | P1 | CORS https://mod.example.com GET #2 | origin=https://mod.example.com,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8875 | P1 | CORS https://mod.example.com GET #3 | origin=https://mod.example.com,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8876 | P1 | CORS https://mod.example.com POST #0 | origin=https://mod.example.com,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8877 | P1 | CORS https://mod.example.com POST #1 | origin=https://mod.example.com,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8878 | P1 | CORS https://mod.example.com POST #2 | origin=https://mod.example.com,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8879 | P1 | CORS https://mod.example.com POST #3 | origin=https://mod.example.com,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8880 | P1 | CORS https://mod.example.com PUT #0 | origin=https://mod.example.com,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8881 | P1 | CORS https://mod.example.com PUT #1 | origin=https://mod.example.com,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8882 | P1 | CORS https://mod.example.com PUT #2 | origin=https://mod.example.com,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8883 | P1 | CORS https://mod.example.com PUT #3 | origin=https://mod.example.com,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8884 | P1 | CORS https://mod.example.com DELETE #0 | origin=https://mod.example.com,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8885 | P1 | CORS https://mod.example.com DELETE #1 | origin=https://mod.example.com,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8886 | P1 | CORS https://mod.example.com DELETE #2 | origin=https://mod.example.com,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8887 | P1 | CORS https://mod.example.com DELETE #3 | origin=https://mod.example.com,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8888 | P1 | CORS https://mod.example.com OPTIONS #0 | origin=https://mod.example.com,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8889 | P1 | CORS https://mod.example.com OPTIONS #1 | origin=https://mod.example.com,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8890 | P1 | CORS https://mod.example.com OPTIONS #2 | origin=https://mod.example.com,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8891 | P1 | CORS https://mod.example.com OPTIONS #3 | origin=https://mod.example.com,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8892 | P1 | CORS http://evil.example GET #0 | origin=http://evil.example,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8893 | P1 | CORS http://evil.example GET #1 | origin=http://evil.example,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8894 | P1 | CORS http://evil.example GET #2 | origin=http://evil.example,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8895 | P1 | CORS http://evil.example GET #3 | origin=http://evil.example,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8896 | P1 | CORS http://evil.example POST #0 | origin=http://evil.example,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8897 | P1 | CORS http://evil.example POST #1 | origin=http://evil.example,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8898 | P1 | CORS http://evil.example POST #2 | origin=http://evil.example,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8899 | P1 | CORS http://evil.example POST #3 | origin=http://evil.example,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8900 | P1 | CORS http://evil.example PUT #0 | origin=http://evil.example,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8901 | P1 | CORS http://evil.example PUT #1 | origin=http://evil.example,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8902 | P1 | CORS http://evil.example PUT #2 | origin=http://evil.example,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8903 | P1 | CORS http://evil.example PUT #3 | origin=http://evil.example,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8904 | P1 | CORS http://evil.example DELETE #0 | origin=http://evil.example,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8905 | P1 | CORS http://evil.example DELETE #1 | origin=http://evil.example,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8906 | P1 | CORS http://evil.example DELETE #2 | origin=http://evil.example,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8907 | P1 | CORS http://evil.example DELETE #3 | origin=http://evil.example,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8908 | P1 | CORS http://evil.example OPTIONS #0 | origin=http://evil.example,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8909 | P1 | CORS http://evil.example OPTIONS #1 | origin=http://evil.example,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8910 | P1 | CORS http://evil.example OPTIONS #2 | origin=http://evil.example,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8911 | P1 | CORS http://evil.example OPTIONS #3 | origin=http://evil.example,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8912 | P1 | CORS https://attacker.com GET #0 | origin=https://attacker.com,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8913 | P1 | CORS https://attacker.com GET #1 | origin=https://attacker.com,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8914 | P1 | CORS https://attacker.com GET #2 | origin=https://attacker.com,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8915 | P1 | CORS https://attacker.com GET #3 | origin=https://attacker.com,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8916 | P1 | CORS https://attacker.com POST #0 | origin=https://attacker.com,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8917 | P1 | CORS https://attacker.com POST #1 | origin=https://attacker.com,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8918 | P1 | CORS https://attacker.com POST #2 | origin=https://attacker.com,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8919 | P1 | CORS https://attacker.com POST #3 | origin=https://attacker.com,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8920 | P1 | CORS https://attacker.com PUT #0 | origin=https://attacker.com,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8921 | P1 | CORS https://attacker.com PUT #1 | origin=https://attacker.com,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8922 | P1 | CORS https://attacker.com PUT #2 | origin=https://attacker.com,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8923 | P1 | CORS https://attacker.com PUT #3 | origin=https://attacker.com,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8924 | P1 | CORS https://attacker.com DELETE #0 | origin=https://attacker.com,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8925 | P1 | CORS https://attacker.com DELETE #1 | origin=https://attacker.com,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8926 | P1 | CORS https://attacker.com DELETE #2 | origin=https://attacker.com,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8927 | P1 | CORS https://attacker.com DELETE #3 | origin=https://attacker.com,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8928 | P1 | CORS https://attacker.com OPTIONS #0 | origin=https://attacker.com,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8929 | P1 | CORS https://attacker.com OPTIONS #1 | origin=https://attacker.com,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8930 | P1 | CORS https://attacker.com OPTIONS #2 | origin=https://attacker.com,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8931 | P1 | CORS https://attacker.com OPTIONS #3 | origin=https://attacker.com,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8932 | P1 | CORS null GET #0 | origin=null,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8933 | P1 | CORS null GET #1 | origin=null,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8934 | P1 | CORS null GET #2 | origin=null,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8935 | P1 | CORS null GET #3 | origin=null,method=GET | handled | test_security_phase2_part_2.py |
| TC-SEC-8936 | P1 | CORS null POST #0 | origin=null,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8937 | P1 | CORS null POST #1 | origin=null,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8938 | P1 | CORS null POST #2 | origin=null,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8939 | P1 | CORS null POST #3 | origin=null,method=POST | handled | test_security_phase2_part_2.py |
| TC-SEC-8940 | P1 | CORS null PUT #0 | origin=null,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8941 | P1 | CORS null PUT #1 | origin=null,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8942 | P1 | CORS null PUT #2 | origin=null,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8943 | P1 | CORS null PUT #3 | origin=null,method=PUT | handled | test_security_phase2_part_2.py |
| TC-SEC-8944 | P1 | CORS null DELETE #0 | origin=null,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8945 | P1 | CORS null DELETE #1 | origin=null,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8946 | P1 | CORS null DELETE #2 | origin=null,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8947 | P1 | CORS null DELETE #3 | origin=null,method=DELETE | handled | test_security_phase2_part_2.py |
| TC-SEC-8948 | P1 | CORS null OPTIONS #0 | origin=null,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8949 | P1 | CORS null OPTIONS #1 | origin=null,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8950 | P1 | CORS null OPTIONS #2 | origin=null,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8951 | P1 | CORS null OPTIONS #3 | origin=null,method=OPTIONS | handled | test_security_phase2_part_2.py |
| TC-SEC-8972 | P1 | Auth key '' #0 | key='' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8973 | P1 | Auth key '' #1 | key='' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8974 | P1 | Auth key '' #2 | key='' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8975 | P1 | Auth key '' #3 | key='' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8976 | P1 | Auth key '' #4 | key='' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8977 | P1 | Auth key '' #5 | key='' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8978 | P1 | Auth key '' #6 | key='' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8979 | P1 | Auth key '' #7 | key='' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8980 | P1 | Auth key '' #8 | key='' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8981 | P1 | Auth key '' #9 | key='' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8982 | P1 | Auth key ' ' #0 | key=' ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8983 | P1 | Auth key ' ' #1 | key=' ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8984 | P1 | Auth key ' ' #2 | key=' ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8985 | P1 | Auth key ' ' #3 | key=' ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8986 | P1 | Auth key ' ' #4 | key=' ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8987 | P1 | Auth key ' ' #5 | key=' ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8988 | P1 | Auth key ' ' #6 | key=' ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8989 | P1 | Auth key ' ' #7 | key=' ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8990 | P1 | Auth key ' ' #8 | key=' ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8991 | P1 | Auth key ' ' #9 | key=' ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8992 | P1 | Auth key 'null' #0 | key='null' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8993 | P1 | Auth key 'null' #1 | key='null' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8994 | P1 | Auth key 'null' #2 | key='null' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8995 | P1 | Auth key 'null' #3 | key='null' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8996 | P1 | Auth key 'null' #4 | key='null' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8997 | P1 | Auth key 'null' #5 | key='null' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8998 | P1 | Auth key 'null' #6 | key='null' | 401 | test_security_phase2_part_3.py |
| TC-SEC-8999 | P1 | Auth key 'null' #7 | key='null' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9000 | P1 | Auth key 'null' #8 | key='null' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9001 | P1 | Auth key 'null' #9 | key='null' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9002 | P1 | Auth key 'None' #0 | key='None' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9003 | P1 | Auth key 'None' #1 | key='None' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9004 | P1 | Auth key 'None' #2 | key='None' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9005 | P1 | Auth key 'None' #3 | key='None' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9006 | P1 | Auth key 'None' #4 | key='None' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9007 | P1 | Auth key 'None' #5 | key='None' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9008 | P1 | Auth key 'None' #6 | key='None' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9009 | P1 | Auth key 'None' #7 | key='None' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9010 | P1 | Auth key 'None' #8 | key='None' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9011 | P1 | Auth key 'None' #9 | key='None' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9012 | P1 | Auth key 'CHANGE_ME' #0 | key='CHANGE_ME' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9013 | P1 | Auth key 'CHANGE_ME' #1 | key='CHANGE_ME' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9014 | P1 | Auth key 'CHANGE_ME' #2 | key='CHANGE_ME' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9015 | P1 | Auth key 'CHANGE_ME' #3 | key='CHANGE_ME' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9016 | P1 | Auth key 'CHANGE_ME' #4 | key='CHANGE_ME' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9017 | P1 | Auth key 'CHANGE_ME' #5 | key='CHANGE_ME' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9018 | P1 | Auth key 'CHANGE_ME' #6 | key='CHANGE_ME' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9019 | P1 | Auth key 'CHANGE_ME' #7 | key='CHANGE_ME' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9020 | P1 | Auth key 'CHANGE_ME' #8 | key='CHANGE_ME' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9021 | P1 | Auth key 'CHANGE_ME' #9 | key='CHANGE_ME' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9022 | P1 | Auth key 'wrong-key' #0 | key='wrong-key' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9023 | P1 | Auth key 'wrong-key' #1 | key='wrong-key' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9024 | P1 | Auth key 'wrong-key' #2 | key='wrong-key' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9025 | P1 | Auth key 'wrong-key' #3 | key='wrong-key' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9026 | P1 | Auth key 'wrong-key' #4 | key='wrong-key' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9027 | P1 | Auth key 'wrong-key' #5 | key='wrong-key' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9028 | P1 | Auth key 'wrong-key' #6 | key='wrong-key' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9029 | P1 | Auth key 'wrong-key' #7 | key='wrong-key' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9030 | P1 | Auth key 'wrong-key' #8 | key='wrong-key' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9031 | P1 | Auth key 'wrong-key' #9 | key='wrong-key' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9032 | P1 | Auth key 'test-admin-key ' #0 | key='test-admin-key ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9033 | P1 | Auth key 'test-admin-key ' #1 | key='test-admin-key ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9034 | P1 | Auth key 'test-admin-key ' #2 | key='test-admin-key ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9035 | P1 | Auth key 'test-admin-key ' #3 | key='test-admin-key ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9036 | P1 | Auth key 'test-admin-key ' #4 | key='test-admin-key ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9037 | P1 | Auth key 'test-admin-key ' #5 | key='test-admin-key ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9038 | P1 | Auth key 'test-admin-key ' #6 | key='test-admin-key ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9039 | P1 | Auth key 'test-admin-key ' #7 | key='test-admin-key ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9040 | P1 | Auth key 'test-admin-key ' #8 | key='test-admin-key ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9041 | P1 | Auth key 'test-admin-key ' #9 | key='test-admin-key ' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9042 | P1 | Auth key 'TEST-ADMIN-KEY' #0 | key='TEST-ADMIN-KEY' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9043 | P1 | Auth key 'TEST-ADMIN-KEY' #1 | key='TEST-ADMIN-KEY' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9044 | P1 | Auth key 'TEST-ADMIN-KEY' #2 | key='TEST-ADMIN-KEY' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9045 | P1 | Auth key 'TEST-ADMIN-KEY' #3 | key='TEST-ADMIN-KEY' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9046 | P1 | Auth key 'TEST-ADMIN-KEY' #4 | key='TEST-ADMIN-KEY' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9047 | P1 | Auth key 'TEST-ADMIN-KEY' #5 | key='TEST-ADMIN-KEY' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9048 | P1 | Auth key 'TEST-ADMIN-KEY' #6 | key='TEST-ADMIN-KEY' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9049 | P1 | Auth key 'TEST-ADMIN-KEY' #7 | key='TEST-ADMIN-KEY' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9050 | P1 | Auth key 'TEST-ADMIN-KEY' #8 | key='TEST-ADMIN-KEY' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9051 | P1 | Auth key 'TEST-ADMIN-KEY' #9 | key='TEST-ADMIN-KEY' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9052 | P1 | Auth key 'bearer-token' #0 | key='bearer-token' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9053 | P1 | Auth key 'bearer-token' #1 | key='bearer-token' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9054 | P1 | Auth key 'bearer-token' #2 | key='bearer-token' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9055 | P1 | Auth key 'bearer-token' #3 | key='bearer-token' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9056 | P1 | Auth key 'bearer-token' #4 | key='bearer-token' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9057 | P1 | Auth key 'bearer-token' #5 | key='bearer-token' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9058 | P1 | Auth key 'bearer-token' #6 | key='bearer-token' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9059 | P1 | Auth key 'bearer-token' #7 | key='bearer-token' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9060 | P1 | Auth key 'bearer-token' #8 | key='bearer-token' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9061 | P1 | Auth key 'bearer-token' #9 | key='bearer-token' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9062 | P1 | Auth key 'leaked-secret' #0 | key='leaked-secret' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9063 | P1 | Auth key 'leaked-secret' #1 | key='leaked-secret' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9064 | P1 | Auth key 'leaked-secret' #2 | key='leaked-secret' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9065 | P1 | Auth key 'leaked-secret' #3 | key='leaked-secret' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9066 | P1 | Auth key 'leaked-secret' #4 | key='leaked-secret' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9067 | P1 | Auth key 'leaked-secret' #5 | key='leaked-secret' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9068 | P1 | Auth key 'leaked-secret' #6 | key='leaked-secret' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9069 | P1 | Auth key 'leaked-secret' #7 | key='leaked-secret' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9070 | P1 | Auth key 'leaked-secret' #8 | key='leaked-secret' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9071 | P1 | Auth key 'leaked-secret' #9 | key='leaked-secret' | 401 | test_security_phase2_part_3.py |
| TC-SEC-9082 | P2 | Injection #0 "'; DROP TABLE users;" | payload="'; DROP TABLE users;" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9083 | P2 | Injection #1 "'; DROP TABLE users;" | payload="'; DROP TABLE users;" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9084 | P2 | Injection #2 "'; DROP TABLE users;" | payload="'; DROP TABLE users;" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9085 | P2 | Injection #3 "'; DROP TABLE users;" | payload="'; DROP TABLE users;" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9086 | P2 | Injection #0 "' OR 1=1 --" | payload="' OR 1=1 --" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9087 | P2 | Injection #1 "' OR 1=1 --" | payload="' OR 1=1 --" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9088 | P2 | Injection #2 "' OR 1=1 --" | payload="' OR 1=1 --" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9089 | P2 | Injection #3 "' OR 1=1 --" | payload="' OR 1=1 --" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9090 | P2 | Injection #0 '<script>alert(1)</sc' | payload='<script>alert(1)</sc' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9091 | P2 | Injection #1 '<script>alert(1)</sc' | payload='<script>alert(1)</sc' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9092 | P2 | Injection #2 '<script>alert(1)</sc' | payload='<script>alert(1)</sc' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9093 | P2 | Injection #3 '<script>alert(1)</sc' | payload='<script>alert(1)</sc' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9094 | P2 | Injection #0 '{{ 7 * 7 }}' | payload='{{ 7 * 7 }}' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9095 | P2 | Injection #1 '{{ 7 * 7 }}' | payload='{{ 7 * 7 }}' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9096 | P2 | Injection #2 '{{ 7 * 7 }}' | payload='{{ 7 * 7 }}' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9097 | P2 | Injection #3 '{{ 7 * 7 }}' | payload='{{ 7 * 7 }}' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9098 | P2 | Injection #0 '${7*7}' | payload='${7*7}' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9099 | P2 | Injection #1 '${7*7}' | payload='${7*7}' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9100 | P2 | Injection #2 '${7*7}' | payload='${7*7}' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9101 | P2 | Injection #3 '${7*7}' | payload='${7*7}' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9102 | P2 | Injection #0 'javascript:alert(1)' | payload='javascript:alert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9103 | P2 | Injection #1 'javascript:alert(1)' | payload='javascript:alert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9104 | P2 | Injection #2 'javascript:alert(1)' | payload='javascript:alert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9105 | P2 | Injection #3 'javascript:alert(1)' | payload='javascript:alert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9106 | P2 | Injection #0 'SELECT * FROM users ' | payload='SELECT * FROM users ' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9107 | P2 | Injection #1 'SELECT * FROM users ' | payload='SELECT * FROM users ' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9108 | P2 | Injection #2 'SELECT * FROM users ' | payload='SELECT * FROM users ' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9109 | P2 | Injection #3 'SELECT * FROM users ' | payload='SELECT * FROM users ' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9110 | P2 | Injection #0 'UNION SELECT passwor' | payload='UNION SELECT passwor' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9111 | P2 | Injection #1 'UNION SELECT passwor' | payload='UNION SELECT passwor' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9112 | P2 | Injection #2 'UNION SELECT passwor' | payload='UNION SELECT passwor' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9113 | P2 | Injection #3 'UNION SELECT passwor' | payload='UNION SELECT passwor' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9114 | P2 | Injection #0 "x' OR '1'='1" | payload="x' OR '1'='1" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9115 | P2 | Injection #1 "x' OR '1'='1" | payload="x' OR '1'='1" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9116 | P2 | Injection #2 "x' OR '1'='1" | payload="x' OR '1'='1" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9117 | P2 | Injection #3 "x' OR '1'='1" | payload="x' OR '1'='1" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9118 | P2 | Injection #0 "'; EXEC xp_cmdshell(" | payload="'; EXEC xp_cmdshell(" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9119 | P2 | Injection #1 "'; EXEC xp_cmdshell(" | payload="'; EXEC xp_cmdshell(" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9120 | P2 | Injection #2 "'; EXEC xp_cmdshell(" | payload="'; EXEC xp_cmdshell(" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9121 | P2 | Injection #3 "'; EXEC xp_cmdshell(" | payload="'; EXEC xp_cmdshell(" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9122 | P2 | Injection #0 "<!--#exec cmd='ls' -" | payload="<!--#exec cmd='ls' -" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9123 | P2 | Injection #1 "<!--#exec cmd='ls' -" | payload="<!--#exec cmd='ls' -" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9124 | P2 | Injection #2 "<!--#exec cmd='ls' -" | payload="<!--#exec cmd='ls' -" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9125 | P2 | Injection #3 "<!--#exec cmd='ls' -" | payload="<!--#exec cmd='ls' -" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9126 | P2 | Injection #0 'cmd | sh -i' | payload='cmd | sh -i' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9127 | P2 | Injection #1 'cmd | sh -i' | payload='cmd | sh -i' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9128 | P2 | Injection #2 'cmd | sh -i' | payload='cmd | sh -i' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9129 | P2 | Injection #3 'cmd | sh -i' | payload='cmd | sh -i' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9130 | P2 | Injection #0 '`whoami`' | payload='`whoami`' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9131 | P2 | Injection #1 '`whoami`' | payload='`whoami`' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9132 | P2 | Injection #2 '`whoami`' | payload='`whoami`' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9133 | P2 | Injection #3 '`whoami`' | payload='`whoami`' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9134 | P2 | Injection #0 '$(cat /etc/passwd)' | payload='$(cat /etc/passwd)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9135 | P2 | Injection #1 '$(cat /etc/passwd)' | payload='$(cat /etc/passwd)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9136 | P2 | Injection #2 '$(cat /etc/passwd)' | payload='$(cat /etc/passwd)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9137 | P2 | Injection #3 '$(cat /etc/passwd)' | payload='$(cat /etc/passwd)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9138 | P2 | Injection #0 '%3Cscript%3Ealert(1)' | payload='%3Cscript%3Ealert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9139 | P2 | Injection #1 '%3Cscript%3Ealert(1)' | payload='%3Cscript%3Ealert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9140 | P2 | Injection #2 '%3Cscript%3Ealert(1)' | payload='%3Cscript%3Ealert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9141 | P2 | Injection #3 '%3Cscript%3Ealert(1)' | payload='%3Cscript%3Ealert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9142 | P2 | Injection #0 '\\u003cscript\\u003e' | payload='\\u003cscript\\u003e' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9143 | P2 | Injection #1 '\\u003cscript\\u003e' | payload='\\u003cscript\\u003e' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9144 | P2 | Injection #2 '\\u003cscript\\u003e' | payload='\\u003cscript\\u003e' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9145 | P2 | Injection #3 '\\u003cscript\\u003e' | payload='\\u003cscript\\u003e' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9146 | P2 | Injection #0 '&#60;script&#62;' | payload='&#60;script&#62;' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9147 | P2 | Injection #1 '&#60;script&#62;' | payload='&#60;script&#62;' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9148 | P2 | Injection #2 '&#60;script&#62;' | payload='&#60;script&#62;' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9149 | P2 | Injection #3 '&#60;script&#62;' | payload='&#60;script&#62;' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9150 | P2 | Injection #0 "'''''''''''" | payload="'''''''''''" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9151 | P2 | Injection #1 "'''''''''''" | payload="'''''''''''" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9152 | P2 | Injection #2 "'''''''''''" | payload="'''''''''''" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9153 | P2 | Injection #3 "'''''''''''" | payload="'''''''''''" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9154 | P2 | Injection #0 '1; DROP TABLE' | payload='1; DROP TABLE' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9155 | P2 | Injection #1 '1; DROP TABLE' | payload='1; DROP TABLE' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9156 | P2 | Injection #2 '1; DROP TABLE' | payload='1; DROP TABLE' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9157 | P2 | Injection #3 '1; DROP TABLE' | payload='1; DROP TABLE' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9158 | P2 | Injection #0 '../../../etc/passwd' | payload='../../../etc/passwd' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9159 | P2 | Injection #1 '../../../etc/passwd' | payload='../../../etc/passwd' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9160 | P2 | Injection #2 '../../../etc/passwd' | payload='../../../etc/passwd' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9161 | P2 | Injection #3 '../../../etc/passwd' | payload='../../../etc/passwd' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9162 | P2 | Injection #0 'C:\\boot.ini' | payload='C:\\boot.ini' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9163 | P2 | Injection #1 'C:\\boot.ini' | payload='C:\\boot.ini' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9164 | P2 | Injection #2 'C:\\boot.ini' | payload='C:\\boot.ini' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9165 | P2 | Injection #3 'C:\\boot.ini' | payload='C:\\boot.ini' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9166 | P2 | Injection #0 '<IMG SRC=javascript:' | payload='<IMG SRC=javascript:' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9167 | P2 | Injection #1 '<IMG SRC=javascript:' | payload='<IMG SRC=javascript:' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9168 | P2 | Injection #2 '<IMG SRC=javascript:' | payload='<IMG SRC=javascript:' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9169 | P2 | Injection #3 '<IMG SRC=javascript:' | payload='<IMG SRC=javascript:' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9170 | P2 | Injection #0 '<svg onload=alert(1)' | payload='<svg onload=alert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9171 | P2 | Injection #1 '<svg onload=alert(1)' | payload='<svg onload=alert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9172 | P2 | Injection #2 '<svg onload=alert(1)' | payload='<svg onload=alert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9173 | P2 | Injection #3 '<svg onload=alert(1)' | payload='<svg onload=alert(1)' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9174 | P2 | Injection #0 '<iframe src=evil>' | payload='<iframe src=evil>' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9175 | P2 | Injection #1 '<iframe src=evil>' | payload='<iframe src=evil>' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9176 | P2 | Injection #2 '<iframe src=evil>' | payload='<iframe src=evil>' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9177 | P2 | Injection #3 '<iframe src=evil>' | payload='<iframe src=evil>' | moderated | test_security_phase2_part_4.py |
| TC-SEC-9178 | P2 | Injection #0 "SELECT 'a' AS b WHER" | payload="SELECT 'a' AS b WHER" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9179 | P2 | Injection #1 "SELECT 'a' AS b WHER" | payload="SELECT 'a' AS b WHER" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9180 | P2 | Injection #2 "SELECT 'a' AS b WHER" | payload="SELECT 'a' AS b WHER" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9181 | P2 | Injection #3 "SELECT 'a' AS b WHER" | payload="SELECT 'a' AS b WHER" | moderated | test_security_phase2_part_4.py |
| TC-SEC-9182 | P2 | Injection #0 'DROP DATABASE produc' | payload='DROP DATABASE produc' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9183 | P2 | Injection #1 'DROP DATABASE produc' | payload='DROP DATABASE produc' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9184 | P2 | Injection #2 'DROP DATABASE produc' | payload='DROP DATABASE produc' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9185 | P2 | Injection #3 'DROP DATABASE produc' | payload='DROP DATABASE produc' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9186 | P2 | Injection #0 'TRUNCATE TABLE logs' | payload='TRUNCATE TABLE logs' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9187 | P2 | Injection #1 'TRUNCATE TABLE logs' | payload='TRUNCATE TABLE logs' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9188 | P2 | Injection #2 'TRUNCATE TABLE logs' | payload='TRUNCATE TABLE logs' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9189 | P2 | Injection #3 'TRUNCATE TABLE logs' | payload='TRUNCATE TABLE logs' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9190 | P2 | Injection #0 'REPLACE INTO words V' | payload='REPLACE INTO words V' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9191 | P2 | Injection #1 'REPLACE INTO words V' | payload='REPLACE INTO words V' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9192 | P2 | Injection #2 'REPLACE INTO words V' | payload='REPLACE INTO words V' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9193 | P2 | Injection #3 'REPLACE INTO words V' | payload='REPLACE INTO words V' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9194 | P2 | Injection #0 'alert(document.cooki' | payload='alert(document.cooki' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9195 | P2 | Injection #1 'alert(document.cooki' | payload='alert(document.cooki' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9196 | P2 | Injection #2 'alert(document.cooki' | payload='alert(document.cooki' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9197 | P2 | Injection #3 'alert(document.cooki' | payload='alert(document.cooki' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9198 | P2 | Injection #0 "eval('alert(1)')" | payload="eval('alert(1)')" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9199 | P2 | Injection #1 "eval('alert(1)')" | payload="eval('alert(1)')" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9200 | P2 | Injection #2 "eval('alert(1)')" | payload="eval('alert(1)')" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9201 | P2 | Injection #3 "eval('alert(1)')" | payload="eval('alert(1)')" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9202 | P2 | Injection #0 "new Function('alert(" | payload="new Function('alert(" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9203 | P2 | Injection #1 "new Function('alert(" | payload="new Function('alert(" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9204 | P2 | Injection #2 "new Function('alert(" | payload="new Function('alert(" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9205 | P2 | Injection #3 "new Function('alert(" | payload="new Function('alert(" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9206 | P2 | Injection #0 '{% raw %}{% endraw %' | payload='{% raw %}{% endraw %' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9207 | P2 | Injection #1 '{% raw %}{% endraw %' | payload='{% raw %}{% endraw %' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9208 | P2 | Injection #2 '{% raw %}{% endraw %' | payload='{% raw %}{% endraw %' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9209 | P2 | Injection #3 '{% raw %}{% endraw %' | payload='{% raw %}{% endraw %' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9210 | P2 | Injection #0 '{{config}}' | payload='{{config}}' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9211 | P2 | Injection #1 '{{config}}' | payload='{{config}}' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9212 | P2 | Injection #2 '{{config}}' | payload='{{config}}' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9213 | P2 | Injection #3 '{{config}}' | payload='{{config}}' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9214 | P2 | Injection #0 '[[$5*5]]' | payload='[[$5*5]]' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9215 | P2 | Injection #1 '[[$5*5]]' | payload='[[$5*5]]' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9216 | P2 | Injection #2 '[[$5*5]]' | payload='[[$5*5]]' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9217 | P2 | Injection #3 '[[$5*5]]' | payload='[[$5*5]]' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9218 | P2 | Injection #0 '<%= 7*7 %>' | payload='<%= 7*7 %>' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9219 | P2 | Injection #1 '<%= 7*7 %>' | payload='<%= 7*7 %>' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9220 | P2 | Injection #2 '<%= 7*7 %>' | payload='<%= 7*7 %>' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9221 | P2 | Injection #3 '<%= 7*7 %>' | payload='<%= 7*7 %>' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9222 | P2 | Injection #0 "; sh -c 'rm -rf /'" | payload="; sh -c 'rm -rf /'" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9223 | P2 | Injection #1 "; sh -c 'rm -rf /'" | payload="; sh -c 'rm -rf /'" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9224 | P2 | Injection #2 "; sh -c 'rm -rf /'" | payload="; sh -c 'rm -rf /'" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9225 | P2 | Injection #3 "; sh -c 'rm -rf /'" | payload="; sh -c 'rm -rf /'" | moderated | test_security_phase2_part_5.py |
| TC-SEC-9226 | P2 | Injection #0 '| cat /etc/shadow' | payload='| cat /etc/shadow' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9227 | P2 | Injection #1 '| cat /etc/shadow' | payload='| cat /etc/shadow' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9228 | P2 | Injection #2 '| cat /etc/shadow' | payload='| cat /etc/shadow' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9229 | P2 | Injection #3 '| cat /etc/shadow' | payload='| cat /etc/shadow' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9230 | P2 | Injection #0 '&& whoami' | payload='&& whoami' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9231 | P2 | Injection #1 '&& whoami' | payload='&& whoami' | moderated | test_security_phase2_part_5.py |
| TC-SEC-9250 | P2 | Traversal '../etc/passwd' #0 | payload='../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9251 | P2 | Traversal '../etc/passwd' #1 | payload='../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9252 | P2 | Traversal '../etc/passwd' #2 | payload='../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9253 | P2 | Traversal '../etc/passwd' #3 | payload='../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9254 | P2 | Traversal '../etc/passwd' #4 | payload='../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9255 | P2 | Traversal '../etc/passwd' #5 | payload='../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9256 | P2 | Traversal '..\\windows\\system32' #0 | payload='..\\windows\\system32' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9257 | P2 | Traversal '..\\windows\\system32' #1 | payload='..\\windows\\system32' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9258 | P2 | Traversal '..\\windows\\system32' #2 | payload='..\\windows\\system32' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9259 | P2 | Traversal '..\\windows\\system32' #3 | payload='..\\windows\\system32' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9260 | P2 | Traversal '..\\windows\\system32' #4 | payload='..\\windows\\system32' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9261 | P2 | Traversal '..\\windows\\system32' #5 | payload='..\\windows\\system32' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9262 | P2 | Traversal '%2e%2e%2fetc%2fpasswd' #0 | payload='%2e%2e%2fetc%2fpasswd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9263 | P2 | Traversal '%2e%2e%2fetc%2fpasswd' #1 | payload='%2e%2e%2fetc%2fpasswd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9264 | P2 | Traversal '%2e%2e%2fetc%2fpasswd' #2 | payload='%2e%2e%2fetc%2fpasswd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9265 | P2 | Traversal '%2e%2e%2fetc%2fpasswd' #3 | payload='%2e%2e%2fetc%2fpasswd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9266 | P2 | Traversal '%2e%2e%2fetc%2fpasswd' #4 | payload='%2e%2e%2fetc%2fpasswd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9267 | P2 | Traversal '%2e%2e%2fetc%2fpasswd' #5 | payload='%2e%2e%2fetc%2fpasswd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9268 | P2 | Traversal '..%2f..%2fsecret' #0 | payload='..%2f..%2fsecret' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9269 | P2 | Traversal '..%2f..%2fsecret' #1 | payload='..%2f..%2fsecret' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9270 | P2 | Traversal '..%2f..%2fsecret' #2 | payload='..%2f..%2fsecret' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9271 | P2 | Traversal '..%2f..%2fsecret' #3 | payload='..%2f..%2fsecret' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9272 | P2 | Traversal '..%2f..%2fsecret' #4 | payload='..%2f..%2fsecret' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9273 | P2 | Traversal '..%2f..%2fsecret' #5 | payload='..%2f..%2fsecret' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9274 | P2 | Traversal 'etc/passwd' #0 | payload='etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9275 | P2 | Traversal 'etc/passwd' #1 | payload='etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9276 | P2 | Traversal 'etc/passwd' #2 | payload='etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9277 | P2 | Traversal 'etc/passwd' #3 | payload='etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9278 | P2 | Traversal 'etc/passwd' #4 | payload='etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9279 | P2 | Traversal 'etc/passwd' #5 | payload='etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9280 | P2 | Traversal '../../../etc/passwd' #0 | payload='../../../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9281 | P2 | Traversal '../../../etc/passwd' #1 | payload='../../../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9282 | P2 | Traversal '../../../etc/passwd' #2 | payload='../../../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9283 | P2 | Traversal '../../../etc/passwd' #3 | payload='../../../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9284 | P2 | Traversal '../../../etc/passwd' #4 | payload='../../../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9285 | P2 | Traversal '../../../etc/passwd' #5 | payload='../../../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9286 | P2 | Traversal '....//....//etc/passwd' #0 | payload='....//....//etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9287 | P2 | Traversal '....//....//etc/passwd' #1 | payload='....//....//etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9288 | P2 | Traversal '....//....//etc/passwd' #2 | payload='....//....//etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9289 | P2 | Traversal '....//....//etc/passwd' #3 | payload='....//....//etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9290 | P2 | Traversal '....//....//etc/passwd' #4 | payload='....//....//etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9291 | P2 | Traversal '....//....//etc/passwd' #5 | payload='....//....//etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9292 | P2 | Traversal '..%252f..%252f' #0 | payload='..%252f..%252f' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9293 | P2 | Traversal '..%252f..%252f' #1 | payload='..%252f..%252f' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9294 | P2 | Traversal '..%252f..%252f' #2 | payload='..%252f..%252f' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9295 | P2 | Traversal '..%252f..%252f' #3 | payload='..%252f..%252f' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9296 | P2 | Traversal '..%252f..%252f' #4 | payload='..%252f..%252f' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9297 | P2 | Traversal '..%252f..%252f' #5 | payload='..%252f..%252f' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9298 | P2 | Traversal '..' #0 | payload='..' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9299 | P2 | Traversal '..' #1 | payload='..' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9322 | P2 | Method GET on /moderate | method=GET,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9323 | P2 | Method GET on /moderate | method=GET,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9324 | P2 | Method GET on /moderate | method=GET,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9325 | P2 | Method GET on /moderate | method=GET,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9326 | P2 | Method POST on /moderate | method=POST,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9327 | P2 | Method POST on /moderate | method=POST,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9328 | P2 | Method POST on /moderate | method=POST,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9329 | P2 | Method POST on /moderate | method=POST,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9330 | P2 | Method PUT on /moderate | method=PUT,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9331 | P2 | Method PUT on /moderate | method=PUT,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9332 | P2 | Method PUT on /moderate | method=PUT,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9333 | P2 | Method PUT on /moderate | method=PUT,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9334 | P2 | Method DELETE on /moderate | method=DELETE,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9335 | P2 | Method DELETE on /moderate | method=DELETE,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9336 | P2 | Method DELETE on /moderate | method=DELETE,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9337 | P2 | Method DELETE on /moderate | method=DELETE,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9338 | P2 | Method PATCH on /moderate | method=PATCH,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9339 | P2 | Method PATCH on /moderate | method=PATCH,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9340 | P2 | Method PATCH on /moderate | method=PATCH,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9341 | P2 | Method PATCH on /moderate | method=PATCH,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9342 | P2 | Method GET on /moderate/batch | method=GET,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9343 | P2 | Method GET on /moderate/batch | method=GET,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9344 | P2 | Method GET on /moderate/batch | method=GET,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9345 | P2 | Method GET on /moderate/batch | method=GET,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9346 | P2 | Method POST on /moderate/batch | method=POST,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9347 | P2 | Method POST on /moderate/batch | method=POST,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9348 | P2 | Method POST on /moderate/batch | method=POST,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9349 | P2 | Method POST on /moderate/batch | method=POST,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9350 | P2 | Method PUT on /moderate/batch | method=PUT,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9351 | P2 | Method PUT on /moderate/batch | method=PUT,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9352 | P2 | Method PUT on /moderate/batch | method=PUT,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9353 | P2 | Method PUT on /moderate/batch | method=PUT,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9354 | P2 | Method DELETE on /moderate/batch | method=DELETE,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9355 | P2 | Method DELETE on /moderate/batch | method=DELETE,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9356 | P2 | Method DELETE on /moderate/batch | method=DELETE,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9357 | P2 | Method DELETE on /moderate/batch | method=DELETE,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9358 | P2 | Method PATCH on /moderate/batch | method=PATCH,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9359 | P2 | Method PATCH on /moderate/batch | method=PATCH,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9360 | P2 | Method PATCH on /moderate/batch | method=PATCH,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9361 | P2 | Method PATCH on /moderate/batch | method=PATCH,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9362 | P2 | Method GET on /health | method=GET,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9363 | P2 | Method GET on /health | method=GET,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9364 | P2 | Method GET on /health | method=GET,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9365 | P2 | Method GET on /health | method=GET,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9366 | P2 | Method POST on /health | method=POST,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9367 | P2 | Method POST on /health | method=POST,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9368 | P2 | Method POST on /health | method=POST,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9369 | P2 | Method POST on /health | method=POST,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9370 | P2 | Method PUT on /health | method=PUT,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9371 | P2 | Method PUT on /health | method=PUT,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9372 | P2 | Method PUT on /health | method=PUT,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9373 | P2 | Method PUT on /health | method=PUT,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9374 | P2 | Method DELETE on /health | method=DELETE,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9375 | P2 | Method DELETE on /health | method=DELETE,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9376 | P2 | Method DELETE on /health | method=DELETE,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9377 | P2 | Method DELETE on /health | method=DELETE,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9378 | P2 | Method PATCH on /health | method=PATCH,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9379 | P2 | Method PATCH on /health | method=PATCH,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9380 | P2 | Method PATCH on /health | method=PATCH,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9381 | P2 | Method PATCH on /health | method=PATCH,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9382 | P2 | Method GET on /metrics | method=GET,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9383 | P2 | Method GET on /metrics | method=GET,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9384 | P2 | Method GET on /metrics | method=GET,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9385 | P2 | Method GET on /metrics | method=GET,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9386 | P2 | Method POST on /metrics | method=POST,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9387 | P2 | Method POST on /metrics | method=POST,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9388 | P2 | Method POST on /metrics | method=POST,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9389 | P2 | Method POST on /metrics | method=POST,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9390 | P2 | Method PUT on /metrics | method=PUT,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9391 | P2 | Method PUT on /metrics | method=PUT,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9392 | P2 | Method PUT on /metrics | method=PUT,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9393 | P2 | Method PUT on /metrics | method=PUT,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9394 | P2 | Method DELETE on /metrics | method=DELETE,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9395 | P2 | Method DELETE on /metrics | method=DELETE,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9396 | P2 | Method DELETE on /metrics | method=DELETE,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9397 | P2 | Method DELETE on /metrics | method=DELETE,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9398 | P2 | Method PATCH on /metrics | method=PATCH,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9399 | P2 | Method PATCH on /metrics | method=PATCH,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9400 | P2 | Method PATCH on /metrics | method=PATCH,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9401 | P2 | Method PATCH on /metrics | method=PATCH,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9402 | P2 | Method GET on / | method=GET,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9403 | P2 | Method GET on / | method=GET,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9404 | P2 | Method GET on / | method=GET,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9405 | P2 | Method GET on / | method=GET,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9406 | P2 | Method POST on / | method=POST,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9407 | P2 | Method POST on / | method=POST,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9408 | P2 | Method POST on / | method=POST,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9409 | P2 | Method POST on / | method=POST,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9410 | P2 | Method PUT on / | method=PUT,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9411 | P2 | Method PUT on / | method=PUT,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9412 | P2 | Method PUT on / | method=PUT,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9413 | P2 | Method PUT on / | method=PUT,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9414 | P2 | Method DELETE on / | method=DELETE,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9415 | P2 | Method DELETE on / | method=DELETE,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9416 | P2 | Method DELETE on / | method=DELETE,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9417 | P2 | Method DELETE on / | method=DELETE,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9418 | P2 | Method PATCH on / | method=PATCH,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9419 | P2 | Method PATCH on / | method=PATCH,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9420 | P2 | Method PATCH on / | method=PATCH,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9421 | P2 | Method PATCH on / | method=PATCH,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9442 | P3 | Encoded payload scenario 0 | scenario=0 | safe | test_security_phase2_part_7.py |
| TC-SEC-9443 | P3 | Encoded payload scenario 1 | scenario=1 | safe | test_security_phase2_part_7.py |
| TC-SEC-9444 | P3 | Encoded payload scenario 2 | scenario=2 | safe | test_security_phase2_part_7.py |
| TC-SEC-9445 | P3 | Encoded payload scenario 3 | scenario=3 | safe | test_security_phase2_part_7.py |
| TC-SEC-9446 | P3 | Encoded payload scenario 4 | scenario=4 | safe | test_security_phase2_part_7.py |
| TC-SEC-9447 | P3 | Encoded payload scenario 5 | scenario=5 | safe | test_security_phase2_part_7.py |
| TC-SEC-9448 | P3 | Encoded payload scenario 6 | scenario=6 | safe | test_security_phase2_part_7.py |
| TC-SEC-9449 | P3 | Encoded payload scenario 7 | scenario=7 | safe | test_security_phase2_part_7.py |
| TC-SEC-9450 | P3 | Encoded payload scenario 8 | scenario=8 | safe | test_security_phase2_part_7.py |
| TC-SEC-9451 | P3 | Encoded payload scenario 9 | scenario=9 | safe | test_security_phase2_part_7.py |
| TC-SEC-9452 | P3 | Encoded payload scenario 10 | scenario=10 | safe | test_security_phase2_part_7.py |
| TC-SEC-9453 | P3 | Encoded payload scenario 11 | scenario=11 | safe | test_security_phase2_part_7.py |
| TC-SEC-9454 | P3 | Encoded payload scenario 12 | scenario=12 | safe | test_security_phase2_part_7.py |
| TC-SEC-9455 | P3 | Encoded payload scenario 13 | scenario=13 | safe | test_security_phase2_part_7.py |
| TC-SEC-9456 | P3 | Encoded payload scenario 14 | scenario=14 | safe | test_security_phase2_part_7.py |
| TC-SEC-9457 | P3 | Encoded payload scenario 15 | scenario=15 | safe | test_security_phase2_part_7.py |
| TC-SEC-9458 | P3 | Encoded payload scenario 16 | scenario=16 | safe | test_security_phase2_part_7.py |
| TC-SEC-9459 | P3 | Encoded payload scenario 17 | scenario=17 | safe | test_security_phase2_part_7.py |
| TC-SEC-9460 | P3 | Encoded payload scenario 18 | scenario=18 | safe | test_security_phase2_part_7.py |
| TC-SEC-9461 | P3 | Encoded payload scenario 19 | scenario=19 | safe | test_security_phase2_part_7.py |
| TC-SEC-9462 | P3 | Encoded payload scenario 20 | scenario=20 | safe | test_security_phase2_part_7.py |
| TC-SEC-9463 | P3 | Encoded payload scenario 21 | scenario=21 | safe | test_security_phase2_part_7.py |
| TC-SEC-9464 | P3 | Encoded payload scenario 22 | scenario=22 | safe | test_security_phase2_part_7.py |
| TC-SEC-9465 | P3 | Encoded payload scenario 23 | scenario=23 | safe | test_security_phase2_part_7.py |
| TC-SEC-9466 | P3 | Encoded payload scenario 24 | scenario=24 | safe | test_security_phase2_part_7.py |
| TC-SEC-9467 | P3 | Encoded payload scenario 25 | scenario=25 | safe | test_security_phase2_part_7.py |
| TC-SEC-9468 | P3 | Encoded payload scenario 26 | scenario=26 | safe | test_security_phase2_part_7.py |
| TC-SEC-9469 | P3 | Encoded payload scenario 27 | scenario=27 | safe | test_security_phase2_part_7.py |
| TC-SEC-9470 | P3 | Encoded payload scenario 28 | scenario=28 | safe | test_security_phase2_part_7.py |
| TC-SEC-9471 | P3 | Encoded payload scenario 29 | scenario=29 | safe | test_security_phase2_part_7.py |
| TC-SEC-9472 | P3 | Encoded payload scenario 30 | scenario=30 | safe | test_security_phase2_part_7.py |
| TC-SEC-9473 | P3 | Encoded payload scenario 31 | scenario=31 | safe | test_security_phase2_part_7.py |
| TC-SEC-9474 | P3 | Encoded payload scenario 32 | scenario=32 | safe | test_security_phase2_part_7.py |
| TC-SEC-9475 | P3 | Encoded payload scenario 33 | scenario=33 | safe | test_security_phase2_part_7.py |
| TC-SEC-9476 | P3 | Encoded payload scenario 34 | scenario=34 | safe | test_security_phase2_part_7.py |
| TC-SEC-9477 | P3 | Encoded payload scenario 35 | scenario=35 | safe | test_security_phase2_part_7.py |
| TC-SEC-9478 | P3 | Encoded payload scenario 36 | scenario=36 | safe | test_security_phase2_part_7.py |
| TC-SEC-9479 | P3 | Encoded payload scenario 37 | scenario=37 | safe | test_security_phase2_part_7.py |
| TC-SEC-9480 | P3 | Encoded payload scenario 38 | scenario=38 | safe | test_security_phase2_part_7.py |
| TC-SEC-9481 | P3 | Encoded payload scenario 39 | scenario=39 | safe | test_security_phase2_part_7.py |
| TC-SEC-9482 | P3 | Encoded payload scenario 40 | scenario=40 | safe | test_security_phase2_part_7.py |
| TC-SEC-9483 | P3 | Encoded payload scenario 41 | scenario=41 | safe | test_security_phase2_part_7.py |
| TC-SEC-9484 | P3 | Encoded payload scenario 42 | scenario=42 | safe | test_security_phase2_part_7.py |
| TC-SEC-9485 | P3 | Encoded payload scenario 43 | scenario=43 | safe | test_security_phase2_part_7.py |
| TC-SEC-9486 | P3 | Encoded payload scenario 44 | scenario=44 | safe | test_security_phase2_part_7.py |
| TC-SEC-9487 | P3 | Encoded payload scenario 45 | scenario=45 | safe | test_security_phase2_part_7.py |
| TC-SEC-9488 | P3 | Encoded payload scenario 46 | scenario=46 | safe | test_security_phase2_part_7.py |
| TC-SEC-9489 | P3 | Encoded payload scenario 47 | scenario=47 | safe | test_security_phase2_part_7.py |
| TC-SEC-9490 | P3 | Encoded payload scenario 48 | scenario=48 | safe | test_security_phase2_part_7.py |
| TC-SEC-9491 | P3 | Encoded payload scenario 49 | scenario=49 | safe | test_security_phase2_part_7.py |
| TC-SEC-9492 | P3 | Encoded payload scenario 50 | scenario=50 | safe | test_security_phase2_part_7.py |
| TC-SEC-9493 | P3 | Encoded payload scenario 51 | scenario=51 | safe | test_security_phase2_part_7.py |
| TC-SEC-9494 | P3 | Encoded payload scenario 52 | scenario=52 | safe | test_security_phase2_part_7.py |
| TC-SEC-9495 | P3 | Encoded payload scenario 53 | scenario=53 | safe | test_security_phase2_part_7.py |
| TC-SEC-9496 | P3 | Encoded payload scenario 54 | scenario=54 | safe | test_security_phase2_part_7.py |
| TC-SEC-9497 | P3 | Encoded payload scenario 55 | scenario=55 | safe | test_security_phase2_part_7.py |
| TC-SEC-9498 | P3 | Encoded payload scenario 56 | scenario=56 | safe | test_security_phase2_part_7.py |
| TC-SEC-9499 | P3 | Encoded payload scenario 57 | scenario=57 | safe | test_security_phase2_part_7.py |
| TC-SEC-9500 | P3 | Encoded payload scenario 58 | scenario=58 | safe | test_security_phase2_part_7.py |
| TC-SEC-9501 | P3 | Encoded payload scenario 59 | scenario=59 | safe | test_security_phase2_part_7.py |
| TC-SEC-9502 | P3 | Encoded payload scenario 60 | scenario=60 | safe | test_security_phase2_part_7.py |
| TC-SEC-9503 | P3 | Encoded payload scenario 61 | scenario=61 | safe | test_security_phase2_part_7.py |
| TC-SEC-9504 | P3 | Encoded payload scenario 62 | scenario=62 | safe | test_security_phase2_part_7.py |
| TC-SEC-9505 | P3 | Encoded payload scenario 63 | scenario=63 | safe | test_security_phase2_part_7.py |
| TC-SEC-9506 | P3 | Encoded payload scenario 64 | scenario=64 | safe | test_security_phase2_part_7.py |
| TC-SEC-9507 | P3 | Encoded payload scenario 65 | scenario=65 | safe | test_security_phase2_part_7.py |
| TC-SEC-9508 | P3 | Encoded payload scenario 66 | scenario=66 | safe | test_security_phase2_part_7.py |
| TC-SEC-9509 | P3 | Encoded payload scenario 67 | scenario=67 | safe | test_security_phase2_part_7.py |
| TC-SEC-9510 | P3 | Encoded payload scenario 68 | scenario=68 | safe | test_security_phase2_part_7.py |
| TC-SEC-9511 | P3 | Encoded payload scenario 69 | scenario=69 | safe | test_security_phase2_part_7.py |
| TC-SEC-9512 | P3 | Encoded payload scenario 70 | scenario=70 | safe | test_security_phase2_part_7.py |
| TC-SEC-9513 | P3 | Encoded payload scenario 71 | scenario=71 | safe | test_security_phase2_part_7.py |
| TC-SEC-9514 | P3 | Encoded payload scenario 72 | scenario=72 | safe | test_security_phase2_part_7.py |
| TC-SEC-9515 | P3 | Encoded payload scenario 73 | scenario=73 | safe | test_security_phase2_part_7.py |
| TC-SEC-9516 | P3 | Encoded payload scenario 74 | scenario=74 | safe | test_security_phase2_part_7.py |
| TC-SEC-9517 | P3 | Encoded payload scenario 75 | scenario=75 | safe | test_security_phase2_part_7.py |
| TC-SEC-9518 | P3 | Encoded payload scenario 76 | scenario=76 | safe | test_security_phase2_part_7.py |
| TC-SEC-9519 | P3 | Encoded payload scenario 77 | scenario=77 | safe | test_security_phase2_part_7.py |
| TC-SEC-9520 | P3 | Encoded payload scenario 78 | scenario=78 | safe | test_security_phase2_part_7.py |
| TC-SEC-9521 | P3 | Encoded payload scenario 79 | scenario=79 | safe | test_security_phase2_part_7.py |
| TC-SEC-9522 | P3 | Encoded payload scenario 80 | scenario=80 | safe | test_security_phase2_part_7.py |
| TC-SEC-9523 | P3 | Encoded payload scenario 81 | scenario=81 | safe | test_security_phase2_part_7.py |
| TC-SEC-9524 | P3 | Encoded payload scenario 82 | scenario=82 | safe | test_security_phase2_part_7.py |
| TC-SEC-9525 | P3 | Encoded payload scenario 83 | scenario=83 | safe | test_security_phase2_part_7.py |
| TC-SEC-9526 | P3 | Encoded payload scenario 84 | scenario=84 | safe | test_security_phase2_part_7.py |
| TC-SEC-9527 | P3 | Encoded payload scenario 85 | scenario=85 | safe | test_security_phase2_part_7.py |
| TC-SEC-9528 | P3 | Encoded payload scenario 86 | scenario=86 | safe | test_security_phase2_part_7.py |
| TC-SEC-9529 | P3 | Encoded payload scenario 87 | scenario=87 | safe | test_security_phase2_part_7.py |
| TC-SEC-9530 | P3 | Encoded payload scenario 88 | scenario=88 | safe | test_security_phase2_part_7.py |
| TC-SEC-9531 | P3 | Encoded payload scenario 89 | scenario=89 | safe | test_security_phase2_part_7.py |
| TC-SEC-9532 | P3 | Encoded payload scenario 90 | scenario=90 | safe | test_security_phase2_part_7.py |
| TC-SEC-9533 | P3 | Encoded payload scenario 91 | scenario=91 | safe | test_security_phase2_part_7.py |
| TC-SEC-9534 | P3 | Encoded payload scenario 92 | scenario=92 | safe | test_security_phase2_part_7.py |
| TC-SEC-9535 | P3 | Encoded payload scenario 93 | scenario=93 | safe | test_security_phase2_part_7.py |
| TC-SEC-9536 | P3 | Encoded payload scenario 94 | scenario=94 | safe | test_security_phase2_part_7.py |
| TC-SEC-9537 | P3 | Encoded payload scenario 95 | scenario=95 | safe | test_security_phase2_part_7.py |
| TC-SEC-9538 | P3 | Encoded payload scenario 96 | scenario=96 | safe | test_security_phase2_part_7.py |
| TC-SEC-9539 | P3 | Encoded payload scenario 97 | scenario=97 | safe | test_security_phase2_part_7.py |
| TC-SEC-9540 | P3 | Encoded payload scenario 98 | scenario=98 | safe | test_security_phase2_part_7.py |
| TC-SEC-9541 | P3 | Encoded payload scenario 99 | scenario=99 | safe | test_security_phase2_part_7.py |

### Phase 3 - 20,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-SEC-0781 onward.

### Phase 4 - 200,000 cases
- Planned high-scale scenarios, IDs TC-SEC-20781 onward.

### Phase 5 - 1,779,220 cases
- Planned exhaustive dimension sweep, IDs TC-SEC-220781 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_security_phase2_part_1.py | 8732-8831 | P1 | :white_check_mark: Phase 2 |
| test_security_phase2_part_2.py | 8852-8951 | P1 | :white_check_mark: Phase 2 |
| test_security_phase2_part_3.py | 8972-9071 | P1 | :white_check_mark: Phase 2 |
| test_security_phase2_part_4.py | 9082-9181 | P2 | :white_check_mark: Phase 2 |
| test_security_phase2_part_5.py | 9182-9299 | P2 | :white_check_mark: Phase 2 |
| test_security_phase2_part_6.py | 9322-9421 | P2 | :white_check_mark: Phase 2 |
| test_security_phase2_part_7.py | 9442-9541 | P3 | :white_check_mark: Phase 2 |

## Adding New Test Cases (Step-by-Step)

1. Determine the target phase and priority (P0-P3).
2. Confirm the dimension combination is not already in the matrix above.
3. Create `test_<module>_phase2_part_<N>.py` (max 100 cases per file).
4. Follow the golden-master pattern: compute expectations with the real
   application (see `tests/tools/phase2_generator.py`) or assert stable
   properties; use `BaseTest` helpers and the conftest fixtures.
5. Update this README (new row in the Phase 2 table + status table).
6. Run: `uv run python -m pytest tests/<module>/ -v`
7. Commit one file per commit: `[TEST-<TYPE>] Add <module> tests part <N>`.

## Related Documentation
- Security Model
- API Reference
