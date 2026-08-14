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
| TC-SEC-8931 | P1 | Header x-content-type-options on GET /health v0 | header=x-content-type-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8932 | P1 | Header x-content-type-options on GET /health v1 | header=x-content-type-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8933 | P1 | Header x-content-type-options on GET /health v2 | header=x-content-type-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8934 | P1 | Header x-content-type-options on GET /health v3 | header=x-content-type-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8935 | P1 | Header x-content-type-options on POST /moderate v0 | header=x-content-type-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8936 | P1 | Header x-content-type-options on POST /moderate v1 | header=x-content-type-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8937 | P1 | Header x-content-type-options on POST /moderate v2 | header=x-content-type-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8938 | P1 | Header x-content-type-options on POST /moderate v3 | header=x-content-type-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8939 | P1 | Header x-content-type-options on GET /metrics v0 | header=x-content-type-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8940 | P1 | Header x-content-type-options on GET /metrics v1 | header=x-content-type-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8941 | P1 | Header x-content-type-options on GET /metrics v2 | header=x-content-type-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8942 | P1 | Header x-content-type-options on GET /metrics v3 | header=x-content-type-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8943 | P1 | Header x-content-type-options on POST /moderate/batch v0 | header=x-content-type-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8944 | P1 | Header x-content-type-options on POST /moderate/batch v1 | header=x-content-type-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8945 | P1 | Header x-content-type-options on POST /moderate/batch v2 | header=x-content-type-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8946 | P1 | Header x-content-type-options on POST /moderate/batch v3 | header=x-content-type-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8947 | P1 | Header x-content-type-options on GET / v0 | header=x-content-type-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8948 | P1 | Header x-content-type-options on GET / v1 | header=x-content-type-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8949 | P1 | Header x-content-type-options on GET / v2 | header=x-content-type-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8950 | P1 | Header x-content-type-options on GET / v3 | header=x-content-type-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8951 | P1 | Header x-frame-options on GET /health v0 | header=x-frame-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8952 | P1 | Header x-frame-options on GET /health v1 | header=x-frame-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8953 | P1 | Header x-frame-options on GET /health v2 | header=x-frame-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8954 | P1 | Header x-frame-options on GET /health v3 | header=x-frame-options,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8955 | P1 | Header x-frame-options on POST /moderate v0 | header=x-frame-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8956 | P1 | Header x-frame-options on POST /moderate v1 | header=x-frame-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8957 | P1 | Header x-frame-options on POST /moderate v2 | header=x-frame-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8958 | P1 | Header x-frame-options on POST /moderate v3 | header=x-frame-options,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8959 | P1 | Header x-frame-options on GET /metrics v0 | header=x-frame-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8960 | P1 | Header x-frame-options on GET /metrics v1 | header=x-frame-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8961 | P1 | Header x-frame-options on GET /metrics v2 | header=x-frame-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8962 | P1 | Header x-frame-options on GET /metrics v3 | header=x-frame-options,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8963 | P1 | Header x-frame-options on POST /moderate/batch v0 | header=x-frame-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8964 | P1 | Header x-frame-options on POST /moderate/batch v1 | header=x-frame-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8965 | P1 | Header x-frame-options on POST /moderate/batch v2 | header=x-frame-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8966 | P1 | Header x-frame-options on POST /moderate/batch v3 | header=x-frame-options,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8967 | P1 | Header x-frame-options on GET / v0 | header=x-frame-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8968 | P1 | Header x-frame-options on GET / v1 | header=x-frame-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8969 | P1 | Header x-frame-options on GET / v2 | header=x-frame-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8970 | P1 | Header x-frame-options on GET / v3 | header=x-frame-options,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8971 | P1 | Header content-security-policy on GET /health v0 | header=content-security-policy,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8972 | P1 | Header content-security-policy on GET /health v1 | header=content-security-policy,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8973 | P1 | Header content-security-policy on GET /health v2 | header=content-security-policy,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8974 | P1 | Header content-security-policy on GET /health v3 | header=content-security-policy,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8975 | P1 | Header content-security-policy on POST /moderate v0 | header=content-security-policy,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8976 | P1 | Header content-security-policy on POST /moderate v1 | header=content-security-policy,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8977 | P1 | Header content-security-policy on POST /moderate v2 | header=content-security-policy,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8978 | P1 | Header content-security-policy on POST /moderate v3 | header=content-security-policy,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8979 | P1 | Header content-security-policy on GET /metrics v0 | header=content-security-policy,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8980 | P1 | Header content-security-policy on GET /metrics v1 | header=content-security-policy,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8981 | P1 | Header content-security-policy on GET /metrics v2 | header=content-security-policy,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8982 | P1 | Header content-security-policy on GET /metrics v3 | header=content-security-policy,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-8983 | P1 | Header content-security-policy on POST /moderate/batch v0 | header=content-security-policy,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8984 | P1 | Header content-security-policy on POST /moderate/batch v1 | header=content-security-policy,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8985 | P1 | Header content-security-policy on POST /moderate/batch v2 | header=content-security-policy,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8986 | P1 | Header content-security-policy on POST /moderate/batch v3 | header=content-security-policy,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-8987 | P1 | Header content-security-policy on GET / v0 | header=content-security-policy,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8988 | P1 | Header content-security-policy on GET / v1 | header=content-security-policy,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8989 | P1 | Header content-security-policy on GET / v2 | header=content-security-policy,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8990 | P1 | Header content-security-policy on GET / v3 | header=content-security-policy,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-8991 | P1 | Header strict-transport-security on GET /health v0 | header=strict-transport-security,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8992 | P1 | Header strict-transport-security on GET /health v1 | header=strict-transport-security,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8993 | P1 | Header strict-transport-security on GET /health v2 | header=strict-transport-security,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8994 | P1 | Header strict-transport-security on GET /health v3 | header=strict-transport-security,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-8995 | P1 | Header strict-transport-security on POST /moderate v0 | header=strict-transport-security,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8996 | P1 | Header strict-transport-security on POST /moderate v1 | header=strict-transport-security,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8997 | P1 | Header strict-transport-security on POST /moderate v2 | header=strict-transport-security,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8998 | P1 | Header strict-transport-security on POST /moderate v3 | header=strict-transport-security,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-8999 | P1 | Header strict-transport-security on GET /metrics v0 | header=strict-transport-security,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-9000 | P1 | Header strict-transport-security on GET /metrics v1 | header=strict-transport-security,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-9001 | P1 | Header strict-transport-security on GET /metrics v2 | header=strict-transport-security,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-9002 | P1 | Header strict-transport-security on GET /metrics v3 | header=strict-transport-security,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-9003 | P1 | Header strict-transport-security on POST /moderate/batch v0 | header=strict-transport-security,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-9004 | P1 | Header strict-transport-security on POST /moderate/batch v1 | header=strict-transport-security,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-9005 | P1 | Header strict-transport-security on POST /moderate/batch v2 | header=strict-transport-security,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-9006 | P1 | Header strict-transport-security on POST /moderate/batch v3 | header=strict-transport-security,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-9007 | P1 | Header strict-transport-security on GET / v0 | header=strict-transport-security,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-9008 | P1 | Header strict-transport-security on GET / v1 | header=strict-transport-security,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-9009 | P1 | Header strict-transport-security on GET / v2 | header=strict-transport-security,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-9010 | P1 | Header strict-transport-security on GET / v3 | header=strict-transport-security,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-9011 | P1 | Header x-xss-protection on GET /health v0 | header=x-xss-protection,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-9012 | P1 | Header x-xss-protection on GET /health v1 | header=x-xss-protection,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-9013 | P1 | Header x-xss-protection on GET /health v2 | header=x-xss-protection,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-9014 | P1 | Header x-xss-protection on GET /health v3 | header=x-xss-protection,endpoint=GET /health | present | test_security_phase2_part_1.py |
| TC-SEC-9015 | P1 | Header x-xss-protection on POST /moderate v0 | header=x-xss-protection,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-9016 | P1 | Header x-xss-protection on POST /moderate v1 | header=x-xss-protection,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-9017 | P1 | Header x-xss-protection on POST /moderate v2 | header=x-xss-protection,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-9018 | P1 | Header x-xss-protection on POST /moderate v3 | header=x-xss-protection,endpoint=POST /moderate | present | test_security_phase2_part_1.py |
| TC-SEC-9019 | P1 | Header x-xss-protection on GET /metrics v0 | header=x-xss-protection,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-9020 | P1 | Header x-xss-protection on GET /metrics v1 | header=x-xss-protection,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-9021 | P1 | Header x-xss-protection on GET /metrics v2 | header=x-xss-protection,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-9022 | P1 | Header x-xss-protection on GET /metrics v3 | header=x-xss-protection,endpoint=GET /metrics | present | test_security_phase2_part_1.py |
| TC-SEC-9023 | P1 | Header x-xss-protection on POST /moderate/batch v0 | header=x-xss-protection,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-9024 | P1 | Header x-xss-protection on POST /moderate/batch v1 | header=x-xss-protection,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-9025 | P1 | Header x-xss-protection on POST /moderate/batch v2 | header=x-xss-protection,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-9026 | P1 | Header x-xss-protection on POST /moderate/batch v3 | header=x-xss-protection,endpoint=POST /moderate/batch | present | test_security_phase2_part_1.py |
| TC-SEC-9027 | P1 | Header x-xss-protection on GET / v0 | header=x-xss-protection,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-9028 | P1 | Header x-xss-protection on GET / v1 | header=x-xss-protection,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-9029 | P1 | Header x-xss-protection on GET / v2 | header=x-xss-protection,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-9030 | P1 | Header x-xss-protection on GET / v3 | header=x-xss-protection,endpoint=GET / | present | test_security_phase2_part_1.py |
| TC-SEC-9051 | P1 | CORS http://localhost:3000 GET /moderate | origin=http://localhost:3000,method=GET,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9052 | P1 | CORS http://localhost:3000 GET /health | origin=http://localhost:3000,method=GET,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9053 | P1 | CORS http://localhost:3000 GET /metrics | origin=http://localhost:3000,method=GET,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9054 | P1 | CORS http://localhost:3000 GET / | origin=http://localhost:3000,method=GET,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9055 | P1 | CORS http://localhost:3000 POST /moderate | origin=http://localhost:3000,method=POST,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9056 | P1 | CORS http://localhost:3000 POST /health | origin=http://localhost:3000,method=POST,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9057 | P1 | CORS http://localhost:3000 POST /metrics | origin=http://localhost:3000,method=POST,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9058 | P1 | CORS http://localhost:3000 POST / | origin=http://localhost:3000,method=POST,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9059 | P1 | CORS http://localhost:3000 PUT /moderate | origin=http://localhost:3000,method=PUT,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9060 | P1 | CORS http://localhost:3000 PUT /health | origin=http://localhost:3000,method=PUT,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9061 | P1 | CORS http://localhost:3000 PUT /metrics | origin=http://localhost:3000,method=PUT,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9062 | P1 | CORS http://localhost:3000 PUT / | origin=http://localhost:3000,method=PUT,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9063 | P1 | CORS http://localhost:3000 DELETE /moderate | origin=http://localhost:3000,method=DELETE,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9064 | P1 | CORS http://localhost:3000 DELETE /health | origin=http://localhost:3000,method=DELETE,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9065 | P1 | CORS http://localhost:3000 DELETE /metrics | origin=http://localhost:3000,method=DELETE,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9066 | P1 | CORS http://localhost:3000 DELETE / | origin=http://localhost:3000,method=DELETE,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9067 | P1 | CORS http://localhost:3000 OPTIONS /moderate | origin=http://localhost:3000,method=OPTIONS,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9068 | P1 | CORS http://localhost:3000 OPTIONS /health | origin=http://localhost:3000,method=OPTIONS,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9069 | P1 | CORS http://localhost:3000 OPTIONS /metrics | origin=http://localhost:3000,method=OPTIONS,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9070 | P1 | CORS http://localhost:3000 OPTIONS / | origin=http://localhost:3000,method=OPTIONS,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9071 | P1 | CORS https://mod.example.com GET /moderate | origin=https://mod.example.com,method=GET,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9072 | P1 | CORS https://mod.example.com GET /health | origin=https://mod.example.com,method=GET,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9073 | P1 | CORS https://mod.example.com GET /metrics | origin=https://mod.example.com,method=GET,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9074 | P1 | CORS https://mod.example.com GET / | origin=https://mod.example.com,method=GET,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9075 | P1 | CORS https://mod.example.com POST /moderate | origin=https://mod.example.com,method=POST,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9076 | P1 | CORS https://mod.example.com POST /health | origin=https://mod.example.com,method=POST,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9077 | P1 | CORS https://mod.example.com POST /metrics | origin=https://mod.example.com,method=POST,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9078 | P1 | CORS https://mod.example.com POST / | origin=https://mod.example.com,method=POST,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9079 | P1 | CORS https://mod.example.com PUT /moderate | origin=https://mod.example.com,method=PUT,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9080 | P1 | CORS https://mod.example.com PUT /health | origin=https://mod.example.com,method=PUT,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9081 | P1 | CORS https://mod.example.com PUT /metrics | origin=https://mod.example.com,method=PUT,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9082 | P1 | CORS https://mod.example.com PUT / | origin=https://mod.example.com,method=PUT,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9083 | P1 | CORS https://mod.example.com DELETE /moderate | origin=https://mod.example.com,method=DELETE,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9084 | P1 | CORS https://mod.example.com DELETE /health | origin=https://mod.example.com,method=DELETE,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9085 | P1 | CORS https://mod.example.com DELETE /metrics | origin=https://mod.example.com,method=DELETE,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9086 | P1 | CORS https://mod.example.com DELETE / | origin=https://mod.example.com,method=DELETE,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9087 | P1 | CORS https://mod.example.com OPTIONS /moderate | origin=https://mod.example.com,method=OPTIONS,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9088 | P1 | CORS https://mod.example.com OPTIONS /health | origin=https://mod.example.com,method=OPTIONS,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9089 | P1 | CORS https://mod.example.com OPTIONS /metrics | origin=https://mod.example.com,method=OPTIONS,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9090 | P1 | CORS https://mod.example.com OPTIONS / | origin=https://mod.example.com,method=OPTIONS,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9091 | P1 | CORS http://evil.example GET /moderate | origin=http://evil.example,method=GET,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9092 | P1 | CORS http://evil.example GET /health | origin=http://evil.example,method=GET,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9093 | P1 | CORS http://evil.example GET /metrics | origin=http://evil.example,method=GET,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9094 | P1 | CORS http://evil.example GET / | origin=http://evil.example,method=GET,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9095 | P1 | CORS http://evil.example POST /moderate | origin=http://evil.example,method=POST,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9096 | P1 | CORS http://evil.example POST /health | origin=http://evil.example,method=POST,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9097 | P1 | CORS http://evil.example POST /metrics | origin=http://evil.example,method=POST,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9098 | P1 | CORS http://evil.example POST / | origin=http://evil.example,method=POST,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9099 | P1 | CORS http://evil.example PUT /moderate | origin=http://evil.example,method=PUT,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9100 | P1 | CORS http://evil.example PUT /health | origin=http://evil.example,method=PUT,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9101 | P1 | CORS http://evil.example PUT /metrics | origin=http://evil.example,method=PUT,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9102 | P1 | CORS http://evil.example PUT / | origin=http://evil.example,method=PUT,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9103 | P1 | CORS http://evil.example DELETE /moderate | origin=http://evil.example,method=DELETE,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9104 | P1 | CORS http://evil.example DELETE /health | origin=http://evil.example,method=DELETE,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9105 | P1 | CORS http://evil.example DELETE /metrics | origin=http://evil.example,method=DELETE,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9106 | P1 | CORS http://evil.example DELETE / | origin=http://evil.example,method=DELETE,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9107 | P1 | CORS http://evil.example OPTIONS /moderate | origin=http://evil.example,method=OPTIONS,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9108 | P1 | CORS http://evil.example OPTIONS /health | origin=http://evil.example,method=OPTIONS,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9109 | P1 | CORS http://evil.example OPTIONS /metrics | origin=http://evil.example,method=OPTIONS,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9110 | P1 | CORS http://evil.example OPTIONS / | origin=http://evil.example,method=OPTIONS,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9111 | P1 | CORS https://attacker.com GET /moderate | origin=https://attacker.com,method=GET,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9112 | P1 | CORS https://attacker.com GET /health | origin=https://attacker.com,method=GET,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9113 | P1 | CORS https://attacker.com GET /metrics | origin=https://attacker.com,method=GET,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9114 | P1 | CORS https://attacker.com GET / | origin=https://attacker.com,method=GET,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9115 | P1 | CORS https://attacker.com POST /moderate | origin=https://attacker.com,method=POST,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9116 | P1 | CORS https://attacker.com POST /health | origin=https://attacker.com,method=POST,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9117 | P1 | CORS https://attacker.com POST /metrics | origin=https://attacker.com,method=POST,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9118 | P1 | CORS https://attacker.com POST / | origin=https://attacker.com,method=POST,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9119 | P1 | CORS https://attacker.com PUT /moderate | origin=https://attacker.com,method=PUT,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9120 | P1 | CORS https://attacker.com PUT /health | origin=https://attacker.com,method=PUT,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9121 | P1 | CORS https://attacker.com PUT /metrics | origin=https://attacker.com,method=PUT,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9122 | P1 | CORS https://attacker.com PUT / | origin=https://attacker.com,method=PUT,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9123 | P1 | CORS https://attacker.com DELETE /moderate | origin=https://attacker.com,method=DELETE,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9124 | P1 | CORS https://attacker.com DELETE /health | origin=https://attacker.com,method=DELETE,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9125 | P1 | CORS https://attacker.com DELETE /metrics | origin=https://attacker.com,method=DELETE,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9126 | P1 | CORS https://attacker.com DELETE / | origin=https://attacker.com,method=DELETE,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9127 | P1 | CORS https://attacker.com OPTIONS /moderate | origin=https://attacker.com,method=OPTIONS,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9128 | P1 | CORS https://attacker.com OPTIONS /health | origin=https://attacker.com,method=OPTIONS,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9129 | P1 | CORS https://attacker.com OPTIONS /metrics | origin=https://attacker.com,method=OPTIONS,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9130 | P1 | CORS https://attacker.com OPTIONS / | origin=https://attacker.com,method=OPTIONS,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9131 | P1 | CORS null GET /moderate | origin=null,method=GET,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9132 | P1 | CORS null GET /health | origin=null,method=GET,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9133 | P1 | CORS null GET /metrics | origin=null,method=GET,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9134 | P1 | CORS null GET / | origin=null,method=GET,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9135 | P1 | CORS null POST /moderate | origin=null,method=POST,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9136 | P1 | CORS null POST /health | origin=null,method=POST,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9137 | P1 | CORS null POST /metrics | origin=null,method=POST,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9138 | P1 | CORS null POST / | origin=null,method=POST,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9139 | P1 | CORS null PUT /moderate | origin=null,method=PUT,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9140 | P1 | CORS null PUT /health | origin=null,method=PUT,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9141 | P1 | CORS null PUT /metrics | origin=null,method=PUT,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9142 | P1 | CORS null PUT / | origin=null,method=PUT,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9143 | P1 | CORS null DELETE /moderate | origin=null,method=DELETE,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9144 | P1 | CORS null DELETE /health | origin=null,method=DELETE,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9145 | P1 | CORS null DELETE /metrics | origin=null,method=DELETE,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9146 | P1 | CORS null DELETE / | origin=null,method=DELETE,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9147 | P1 | CORS null OPTIONS /moderate | origin=null,method=OPTIONS,path=/moderate | handled | test_security_phase2_part_2.py |
| TC-SEC-9148 | P1 | CORS null OPTIONS /health | origin=null,method=OPTIONS,path=/health | handled | test_security_phase2_part_2.py |
| TC-SEC-9149 | P1 | CORS null OPTIONS /metrics | origin=null,method=OPTIONS,path=/metrics | handled | test_security_phase2_part_2.py |
| TC-SEC-9150 | P1 | CORS null OPTIONS / | origin=null,method=OPTIONS,path=/ | handled | test_security_phase2_part_2.py |
| TC-SEC-9171 | P1 | Auth key '' on /admin/wordbank/stats | key='',endpoint=/admin/wordbank/stats | 401 | test_security_phase2_part_3.py |
| TC-SEC-9172 | P1 | Auth key '' on /admin/wordbank/words | key='',endpoint=/admin/wordbank/words | 401 | test_security_phase2_part_3.py |
| TC-SEC-9173 | P1 | Auth key '' on /admin/wordbank/export | key='',endpoint=/admin/wordbank/export | 401 | test_security_phase2_part_3.py |
| TC-SEC-9174 | P1 | Auth key '' on /admin/wordbank/languages | key='',endpoint=/admin/wordbank/languages | 401 | test_security_phase2_part_3.py |
| TC-SEC-9175 | P1 | Auth key '' on /admin/wordbank/categories | key='',endpoint=/admin/wordbank/categories | 401 | test_security_phase2_part_3.py |
| TC-SEC-9176 | P1 | Auth key '' on /admin/app-config | key='',endpoint=/admin/app-config | 401 | test_security_phase2_part_3.py |
| TC-SEC-9177 | P1 | Auth key '' on /admin/settings | key='',endpoint=/admin/settings | 401 | test_security_phase2_part_3.py |
| TC-SEC-9178 | P1 | Auth key '' on /admin/logs | key='',endpoint=/admin/logs | 401 | test_security_phase2_part_3.py |
| TC-SEC-9179 | P1 | Auth key '' on /admin/health | key='',endpoint=/admin/health | 401 | test_security_phase2_part_3.py |
| TC-SEC-9180 | P1 | Auth key '' on /admin/spot-check | key='',endpoint=/admin/spot-check | 401 | test_security_phase2_part_3.py |
| TC-SEC-9181 | P1 | Auth key ' ' on /admin/wordbank/stats | key=' ',endpoint=/admin/wordbank/stats | 401 | test_security_phase2_part_3.py |
| TC-SEC-9182 | P1 | Auth key ' ' on /admin/wordbank/words | key=' ',endpoint=/admin/wordbank/words | 401 | test_security_phase2_part_3.py |
| TC-SEC-9183 | P1 | Auth key ' ' on /admin/wordbank/export | key=' ',endpoint=/admin/wordbank/export | 401 | test_security_phase2_part_3.py |
| TC-SEC-9184 | P1 | Auth key ' ' on /admin/wordbank/languages | key=' ',endpoint=/admin/wordbank/languages | 401 | test_security_phase2_part_3.py |
| TC-SEC-9185 | P1 | Auth key ' ' on /admin/wordbank/categories | key=' ',endpoint=/admin/wordbank/categories | 401 | test_security_phase2_part_3.py |
| TC-SEC-9186 | P1 | Auth key ' ' on /admin/app-config | key=' ',endpoint=/admin/app-config | 401 | test_security_phase2_part_3.py |
| TC-SEC-9187 | P1 | Auth key ' ' on /admin/settings | key=' ',endpoint=/admin/settings | 401 | test_security_phase2_part_3.py |
| TC-SEC-9188 | P1 | Auth key ' ' on /admin/logs | key=' ',endpoint=/admin/logs | 401 | test_security_phase2_part_3.py |
| TC-SEC-9189 | P1 | Auth key ' ' on /admin/health | key=' ',endpoint=/admin/health | 401 | test_security_phase2_part_3.py |
| TC-SEC-9190 | P1 | Auth key ' ' on /admin/spot-check | key=' ',endpoint=/admin/spot-check | 401 | test_security_phase2_part_3.py |
| TC-SEC-9191 | P1 | Auth key 'null' on /admin/wordbank/stats | key='null',endpoint=/admin/wordbank/stats | 401 | test_security_phase2_part_3.py |
| TC-SEC-9192 | P1 | Auth key 'null' on /admin/wordbank/words | key='null',endpoint=/admin/wordbank/words | 401 | test_security_phase2_part_3.py |
| TC-SEC-9193 | P1 | Auth key 'null' on /admin/wordbank/export | key='null',endpoint=/admin/wordbank/export | 401 | test_security_phase2_part_3.py |
| TC-SEC-9194 | P1 | Auth key 'null' on /admin/wordbank/languages | key='null',endpoint=/admin/wordbank/languages | 401 | test_security_phase2_part_3.py |
| TC-SEC-9195 | P1 | Auth key 'null' on /admin/wordbank/categories | key='null',endpoint=/admin/wordbank/categories | 401 | test_security_phase2_part_3.py |
| TC-SEC-9196 | P1 | Auth key 'null' on /admin/app-config | key='null',endpoint=/admin/app-config | 401 | test_security_phase2_part_3.py |
| TC-SEC-9197 | P1 | Auth key 'null' on /admin/settings | key='null',endpoint=/admin/settings | 401 | test_security_phase2_part_3.py |
| TC-SEC-9198 | P1 | Auth key 'null' on /admin/logs | key='null',endpoint=/admin/logs | 401 | test_security_phase2_part_3.py |
| TC-SEC-9199 | P1 | Auth key 'null' on /admin/health | key='null',endpoint=/admin/health | 401 | test_security_phase2_part_3.py |
| TC-SEC-9200 | P1 | Auth key 'null' on /admin/spot-check | key='null',endpoint=/admin/spot-check | 401 | test_security_phase2_part_3.py |
| TC-SEC-9201 | P1 | Auth key 'None' on /admin/wordbank/stats | key='None',endpoint=/admin/wordbank/stats | 401 | test_security_phase2_part_3.py |
| TC-SEC-9202 | P1 | Auth key 'None' on /admin/wordbank/words | key='None',endpoint=/admin/wordbank/words | 401 | test_security_phase2_part_3.py |
| TC-SEC-9203 | P1 | Auth key 'None' on /admin/wordbank/export | key='None',endpoint=/admin/wordbank/export | 401 | test_security_phase2_part_3.py |
| TC-SEC-9204 | P1 | Auth key 'None' on /admin/wordbank/languages | key='None',endpoint=/admin/wordbank/languages | 401 | test_security_phase2_part_3.py |
| TC-SEC-9205 | P1 | Auth key 'None' on /admin/wordbank/categories | key='None',endpoint=/admin/wordbank/categories | 401 | test_security_phase2_part_3.py |
| TC-SEC-9206 | P1 | Auth key 'None' on /admin/app-config | key='None',endpoint=/admin/app-config | 401 | test_security_phase2_part_3.py |
| TC-SEC-9207 | P1 | Auth key 'None' on /admin/settings | key='None',endpoint=/admin/settings | 401 | test_security_phase2_part_3.py |
| TC-SEC-9208 | P1 | Auth key 'None' on /admin/logs | key='None',endpoint=/admin/logs | 401 | test_security_phase2_part_3.py |
| TC-SEC-9209 | P1 | Auth key 'None' on /admin/health | key='None',endpoint=/admin/health | 401 | test_security_phase2_part_3.py |
| TC-SEC-9210 | P1 | Auth key 'None' on /admin/spot-check | key='None',endpoint=/admin/spot-check | 401 | test_security_phase2_part_3.py |
| TC-SEC-9211 | P1 | Auth key 'CHANGE_ME' on /admin/wordbank/stats | key='CHANGE_ME',endpoint=/admin/wordbank/stats | 401 | test_security_phase2_part_3.py |
| TC-SEC-9212 | P1 | Auth key 'CHANGE_ME' on /admin/wordbank/words | key='CHANGE_ME',endpoint=/admin/wordbank/words | 401 | test_security_phase2_part_3.py |
| TC-SEC-9213 | P1 | Auth key 'CHANGE_ME' on /admin/wordbank/export | key='CHANGE_ME',endpoint=/admin/wordbank/export | 401 | test_security_phase2_part_3.py |
| TC-SEC-9214 | P1 | Auth key 'CHANGE_ME' on /admin/wordbank/languages | key='CHANGE_ME',endpoint=/admin/wordbank/languages | 401 | test_security_phase2_part_3.py |
| TC-SEC-9215 | P1 | Auth key 'CHANGE_ME' on /admin/wordbank/categories | key='CHANGE_ME',endpoint=/admin/wordbank/categories | 401 | test_security_phase2_part_3.py |
| TC-SEC-9216 | P1 | Auth key 'CHANGE_ME' on /admin/app-config | key='CHANGE_ME',endpoint=/admin/app-config | 401 | test_security_phase2_part_3.py |
| TC-SEC-9217 | P1 | Auth key 'CHANGE_ME' on /admin/settings | key='CHANGE_ME',endpoint=/admin/settings | 401 | test_security_phase2_part_3.py |
| TC-SEC-9218 | P1 | Auth key 'CHANGE_ME' on /admin/logs | key='CHANGE_ME',endpoint=/admin/logs | 401 | test_security_phase2_part_3.py |
| TC-SEC-9219 | P1 | Auth key 'CHANGE_ME' on /admin/health | key='CHANGE_ME',endpoint=/admin/health | 401 | test_security_phase2_part_3.py |
| TC-SEC-9220 | P1 | Auth key 'CHANGE_ME' on /admin/spot-check | key='CHANGE_ME',endpoint=/admin/spot-check | 401 | test_security_phase2_part_3.py |
| TC-SEC-9221 | P1 | Auth key 'wrong-key' on /admin/wordbank/stats | key='wrong-key',endpoint=/admin/wordbank/stats | 401 | test_security_phase2_part_3.py |
| TC-SEC-9222 | P1 | Auth key 'wrong-key' on /admin/wordbank/words | key='wrong-key',endpoint=/admin/wordbank/words | 401 | test_security_phase2_part_3.py |
| TC-SEC-9223 | P1 | Auth key 'wrong-key' on /admin/wordbank/export | key='wrong-key',endpoint=/admin/wordbank/export | 401 | test_security_phase2_part_3.py |
| TC-SEC-9224 | P1 | Auth key 'wrong-key' on /admin/wordbank/languages | key='wrong-key',endpoint=/admin/wordbank/languages | 401 | test_security_phase2_part_3.py |
| TC-SEC-9225 | P1 | Auth key 'wrong-key' on /admin/wordbank/categories | key='wrong-key',endpoint=/admin/wordbank/categories | 401 | test_security_phase2_part_3.py |
| TC-SEC-9226 | P1 | Auth key 'wrong-key' on /admin/app-config | key='wrong-key',endpoint=/admin/app-config | 401 | test_security_phase2_part_3.py |
| TC-SEC-9227 | P1 | Auth key 'wrong-key' on /admin/settings | key='wrong-key',endpoint=/admin/settings | 401 | test_security_phase2_part_3.py |
| TC-SEC-9228 | P1 | Auth key 'wrong-key' on /admin/logs | key='wrong-key',endpoint=/admin/logs | 401 | test_security_phase2_part_3.py |
| TC-SEC-9229 | P1 | Auth key 'wrong-key' on /admin/health | key='wrong-key',endpoint=/admin/health | 401 | test_security_phase2_part_3.py |
| TC-SEC-9230 | P1 | Auth key 'wrong-key' on /admin/spot-check | key='wrong-key',endpoint=/admin/spot-check | 401 | test_security_phase2_part_3.py |
| TC-SEC-9231 | P1 | Auth key 'test-admin-key ' on /admin/wordbank/stats | key='test-admin-key ',endpoint=/admin/wordbank/stats | 401 | test_security_phase2_part_3.py |
| TC-SEC-9232 | P1 | Auth key 'test-admin-key ' on /admin/wordbank/words | key='test-admin-key ',endpoint=/admin/wordbank/words | 401 | test_security_phase2_part_3.py |
| TC-SEC-9233 | P1 | Auth key 'test-admin-key ' on /admin/wordbank/export | key='test-admin-key ',endpoint=/admin/wordbank/export | 401 | test_security_phase2_part_3.py |
| TC-SEC-9234 | P1 | Auth key 'test-admin-key ' on /admin/wordbank/languages | key='test-admin-key ',endpoint=/admin/wordbank/languages | 401 | test_security_phase2_part_3.py |
| TC-SEC-9235 | P1 | Auth key 'test-admin-key ' on /admin/wordbank/categories | key='test-admin-key ',endpoint=/admin/wordbank/categories | 401 | test_security_phase2_part_3.py |
| TC-SEC-9236 | P1 | Auth key 'test-admin-key ' on /admin/app-config | key='test-admin-key ',endpoint=/admin/app-config | 401 | test_security_phase2_part_3.py |
| TC-SEC-9237 | P1 | Auth key 'test-admin-key ' on /admin/settings | key='test-admin-key ',endpoint=/admin/settings | 401 | test_security_phase2_part_3.py |
| TC-SEC-9238 | P1 | Auth key 'test-admin-key ' on /admin/logs | key='test-admin-key ',endpoint=/admin/logs | 401 | test_security_phase2_part_3.py |
| TC-SEC-9239 | P1 | Auth key 'test-admin-key ' on /admin/health | key='test-admin-key ',endpoint=/admin/health | 401 | test_security_phase2_part_3.py |
| TC-SEC-9240 | P1 | Auth key 'test-admin-key ' on /admin/spot-check | key='test-admin-key ',endpoint=/admin/spot-check | 401 | test_security_phase2_part_3.py |
| TC-SEC-9241 | P1 | Auth key 'TEST-ADMIN-KEY' on /admin/wordbank/stats | key='TEST-ADMIN-KEY',endpoint=/admin/wordbank/stats | 401 | test_security_phase2_part_3.py |
| TC-SEC-9242 | P1 | Auth key 'TEST-ADMIN-KEY' on /admin/wordbank/words | key='TEST-ADMIN-KEY',endpoint=/admin/wordbank/words | 401 | test_security_phase2_part_3.py |
| TC-SEC-9243 | P1 | Auth key 'TEST-ADMIN-KEY' on /admin/wordbank/export | key='TEST-ADMIN-KEY',endpoint=/admin/wordbank/export | 401 | test_security_phase2_part_3.py |
| TC-SEC-9244 | P1 | Auth key 'TEST-ADMIN-KEY' on /admin/wordbank/languages | key='TEST-ADMIN-KEY',endpoint=/admin/wordbank/languages | 401 | test_security_phase2_part_3.py |
| TC-SEC-9245 | P1 | Auth key 'TEST-ADMIN-KEY' on /admin/wordbank/categories | key='TEST-ADMIN-KEY',endpoint=/admin/wordbank/categories | 401 | test_security_phase2_part_3.py |
| TC-SEC-9246 | P1 | Auth key 'TEST-ADMIN-KEY' on /admin/app-config | key='TEST-ADMIN-KEY',endpoint=/admin/app-config | 401 | test_security_phase2_part_3.py |
| TC-SEC-9247 | P1 | Auth key 'TEST-ADMIN-KEY' on /admin/settings | key='TEST-ADMIN-KEY',endpoint=/admin/settings | 401 | test_security_phase2_part_3.py |
| TC-SEC-9248 | P1 | Auth key 'TEST-ADMIN-KEY' on /admin/logs | key='TEST-ADMIN-KEY',endpoint=/admin/logs | 401 | test_security_phase2_part_3.py |
| TC-SEC-9249 | P1 | Auth key 'TEST-ADMIN-KEY' on /admin/health | key='TEST-ADMIN-KEY',endpoint=/admin/health | 401 | test_security_phase2_part_3.py |
| TC-SEC-9250 | P1 | Auth key 'TEST-ADMIN-KEY' on /admin/spot-check | key='TEST-ADMIN-KEY',endpoint=/admin/spot-check | 401 | test_security_phase2_part_3.py |
| TC-SEC-9251 | P1 | Auth key 'bearer-token' on /admin/wordbank/stats | key='bearer-token',endpoint=/admin/wordbank/stats | 401 | test_security_phase2_part_3.py |
| TC-SEC-9252 | P1 | Auth key 'bearer-token' on /admin/wordbank/words | key='bearer-token',endpoint=/admin/wordbank/words | 401 | test_security_phase2_part_3.py |
| TC-SEC-9253 | P1 | Auth key 'bearer-token' on /admin/wordbank/export | key='bearer-token',endpoint=/admin/wordbank/export | 401 | test_security_phase2_part_3.py |
| TC-SEC-9254 | P1 | Auth key 'bearer-token' on /admin/wordbank/languages | key='bearer-token',endpoint=/admin/wordbank/languages | 401 | test_security_phase2_part_3.py |
| TC-SEC-9255 | P1 | Auth key 'bearer-token' on /admin/wordbank/categories | key='bearer-token',endpoint=/admin/wordbank/categories | 401 | test_security_phase2_part_3.py |
| TC-SEC-9256 | P1 | Auth key 'bearer-token' on /admin/app-config | key='bearer-token',endpoint=/admin/app-config | 401 | test_security_phase2_part_3.py |
| TC-SEC-9257 | P1 | Auth key 'bearer-token' on /admin/settings | key='bearer-token',endpoint=/admin/settings | 401 | test_security_phase2_part_3.py |
| TC-SEC-9258 | P1 | Auth key 'bearer-token' on /admin/logs | key='bearer-token',endpoint=/admin/logs | 401 | test_security_phase2_part_3.py |
| TC-SEC-9259 | P1 | Auth key 'bearer-token' on /admin/health | key='bearer-token',endpoint=/admin/health | 401 | test_security_phase2_part_3.py |
| TC-SEC-9260 | P1 | Auth key 'bearer-token' on /admin/spot-check | key='bearer-token',endpoint=/admin/spot-check | 401 | test_security_phase2_part_3.py |
| TC-SEC-9261 | P1 | Auth key 'leaked-secret' on /admin/wordbank/stats | key='leaked-secret',endpoint=/admin/wordbank/stats | 401 | test_security_phase2_part_3.py |
| TC-SEC-9262 | P1 | Auth key 'leaked-secret' on /admin/wordbank/words | key='leaked-secret',endpoint=/admin/wordbank/words | 401 | test_security_phase2_part_3.py |
| TC-SEC-9263 | P1 | Auth key 'leaked-secret' on /admin/wordbank/export | key='leaked-secret',endpoint=/admin/wordbank/export | 401 | test_security_phase2_part_3.py |
| TC-SEC-9264 | P1 | Auth key 'leaked-secret' on /admin/wordbank/languages | key='leaked-secret',endpoint=/admin/wordbank/languages | 401 | test_security_phase2_part_3.py |
| TC-SEC-9265 | P1 | Auth key 'leaked-secret' on /admin/wordbank/categories | key='leaked-secret',endpoint=/admin/wordbank/categories | 401 | test_security_phase2_part_3.py |
| TC-SEC-9266 | P1 | Auth key 'leaked-secret' on /admin/app-config | key='leaked-secret',endpoint=/admin/app-config | 401 | test_security_phase2_part_3.py |
| TC-SEC-9267 | P1 | Auth key 'leaked-secret' on /admin/settings | key='leaked-secret',endpoint=/admin/settings | 401 | test_security_phase2_part_3.py |
| TC-SEC-9268 | P1 | Auth key 'leaked-secret' on /admin/logs | key='leaked-secret',endpoint=/admin/logs | 401 | test_security_phase2_part_3.py |
| TC-SEC-9269 | P1 | Auth key 'leaked-secret' on /admin/health | key='leaked-secret',endpoint=/admin/health | 401 | test_security_phase2_part_3.py |
| TC-SEC-9270 | P1 | Auth key 'leaked-secret' on /admin/spot-check | key='leaked-secret',endpoint=/admin/spot-check | 401 | test_security_phase2_part_3.py |
| TC-SEC-9281 | P2 | Injection raw "'; DROP TABLE users;" | payload="'; DROP TABLE users;",variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9282 | P2 | Injection quoted "'; DROP TABLE users;" | payload="'; DROP TABLE users;",variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9283 | P2 | Injection html "'; DROP TABLE users;" | payload="'; DROP TABLE users;",variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9284 | P2 | Injection unicode "'; DROP TABLE users;" | payload="'; DROP TABLE users;",variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9285 | P2 | Injection raw "' OR 1=1 --" | payload="' OR 1=1 --",variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9286 | P2 | Injection quoted "' OR 1=1 --" | payload="' OR 1=1 --",variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9287 | P2 | Injection html "' OR 1=1 --" | payload="' OR 1=1 --",variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9288 | P2 | Injection unicode "' OR 1=1 --" | payload="' OR 1=1 --",variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9289 | P2 | Injection raw '<script>alert(1)</sc' | payload='<script>alert(1)</sc',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9290 | P2 | Injection quoted '<script>alert(1)</sc' | payload='<script>alert(1)</sc',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9291 | P2 | Injection html '<script>alert(1)</sc' | payload='<script>alert(1)</sc',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9292 | P2 | Injection unicode '<script>alert(1)</sc' | payload='<script>alert(1)</sc',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9293 | P2 | Injection raw '{{ 7 * 7 }}' | payload='{{ 7 * 7 }}',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9294 | P2 | Injection quoted '{{ 7 * 7 }}' | payload='{{ 7 * 7 }}',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9295 | P2 | Injection html '{{ 7 * 7 }}' | payload='{{ 7 * 7 }}',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9296 | P2 | Injection unicode '{{ 7 * 7 }}' | payload='{{ 7 * 7 }}',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9297 | P2 | Injection raw '${7*7}' | payload='${7*7}',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9298 | P2 | Injection quoted '${7*7}' | payload='${7*7}',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9299 | P2 | Injection html '${7*7}' | payload='${7*7}',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9300 | P2 | Injection unicode '${7*7}' | payload='${7*7}',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9301 | P2 | Injection raw 'javascript:alert(1)' | payload='javascript:alert(1)',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9302 | P2 | Injection quoted 'javascript:alert(1)' | payload='javascript:alert(1)',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9303 | P2 | Injection html 'javascript:alert(1)' | payload='javascript:alert(1)',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9304 | P2 | Injection unicode 'javascript:alert(1)' | payload='javascript:alert(1)',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9305 | P2 | Injection raw 'SELECT * FROM users ' | payload='SELECT * FROM users ',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9306 | P2 | Injection quoted 'SELECT * FROM users ' | payload='SELECT * FROM users ',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9307 | P2 | Injection html 'SELECT * FROM users ' | payload='SELECT * FROM users ',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9308 | P2 | Injection unicode 'SELECT * FROM users ' | payload='SELECT * FROM users ',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9309 | P2 | Injection raw 'UNION SELECT passwor' | payload='UNION SELECT passwor',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9310 | P2 | Injection quoted 'UNION SELECT passwor' | payload='UNION SELECT passwor',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9311 | P2 | Injection html 'UNION SELECT passwor' | payload='UNION SELECT passwor',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9312 | P2 | Injection unicode 'UNION SELECT passwor' | payload='UNION SELECT passwor',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9313 | P2 | Injection raw "x' OR '1'='1" | payload="x' OR '1'='1",variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9314 | P2 | Injection quoted "x' OR '1'='1" | payload="x' OR '1'='1",variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9315 | P2 | Injection html "x' OR '1'='1" | payload="x' OR '1'='1",variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9316 | P2 | Injection unicode "x' OR '1'='1" | payload="x' OR '1'='1",variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9317 | P2 | Injection raw "'; EXEC xp_cmdshell(" | payload="'; EXEC xp_cmdshell(",variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9318 | P2 | Injection quoted "'; EXEC xp_cmdshell(" | payload="'; EXEC xp_cmdshell(",variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9319 | P2 | Injection html "'; EXEC xp_cmdshell(" | payload="'; EXEC xp_cmdshell(",variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9320 | P2 | Injection unicode "'; EXEC xp_cmdshell(" | payload="'; EXEC xp_cmdshell(",variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9321 | P2 | Injection raw "<!--#exec cmd='ls' -" | payload="<!--#exec cmd='ls' -",variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9322 | P2 | Injection quoted "<!--#exec cmd='ls' -" | payload="<!--#exec cmd='ls' -",variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9323 | P2 | Injection html "<!--#exec cmd='ls' -" | payload="<!--#exec cmd='ls' -",variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9324 | P2 | Injection unicode "<!--#exec cmd='ls' -" | payload="<!--#exec cmd='ls' -",variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9325 | P2 | Injection raw 'cmd | sh -i' | payload='cmd | sh -i',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9326 | P2 | Injection quoted 'cmd | sh -i' | payload='cmd | sh -i',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9327 | P2 | Injection html 'cmd | sh -i' | payload='cmd | sh -i',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9328 | P2 | Injection unicode 'cmd | sh -i' | payload='cmd | sh -i',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9329 | P2 | Injection raw '`whoami`' | payload='`whoami`',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9330 | P2 | Injection quoted '`whoami`' | payload='`whoami`',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9331 | P2 | Injection html '`whoami`' | payload='`whoami`',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9332 | P2 | Injection unicode '`whoami`' | payload='`whoami`',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9333 | P2 | Injection raw '$(cat /etc/passwd)' | payload='$(cat /etc/passwd)',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9334 | P2 | Injection quoted '$(cat /etc/passwd)' | payload='$(cat /etc/passwd)',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9335 | P2 | Injection html '$(cat /etc/passwd)' | payload='$(cat /etc/passwd)',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9336 | P2 | Injection unicode '$(cat /etc/passwd)' | payload='$(cat /etc/passwd)',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9337 | P2 | Injection raw '%3Cscript%3Ealert(1)' | payload='%3Cscript%3Ealert(1)',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9338 | P2 | Injection quoted '%3Cscript%3Ealert(1)' | payload='%3Cscript%3Ealert(1)',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9339 | P2 | Injection html '%3Cscript%3Ealert(1)' | payload='%3Cscript%3Ealert(1)',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9340 | P2 | Injection unicode '%3Cscript%3Ealert(1)' | payload='%3Cscript%3Ealert(1)',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9341 | P2 | Injection raw '\\u003cscript\\u003e' | payload='\\u003cscript\\u003e',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9342 | P2 | Injection quoted '\\u003cscript\\u003e' | payload='\\u003cscript\\u003e',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9343 | P2 | Injection html '\\u003cscript\\u003e' | payload='\\u003cscript\\u003e',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9344 | P2 | Injection unicode '\\u003cscript\\u003e' | payload='\\u003cscript\\u003e',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9345 | P2 | Injection raw '&#60;script&#62;' | payload='&#60;script&#62;',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9346 | P2 | Injection quoted '&#60;script&#62;' | payload='&#60;script&#62;',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9347 | P2 | Injection html '&#60;script&#62;' | payload='&#60;script&#62;',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9348 | P2 | Injection unicode '&#60;script&#62;' | payload='&#60;script&#62;',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9349 | P2 | Injection raw "'''''''''''" | payload="'''''''''''",variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9350 | P2 | Injection quoted "'''''''''''" | payload="'''''''''''",variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9351 | P2 | Injection html "'''''''''''" | payload="'''''''''''",variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9352 | P2 | Injection unicode "'''''''''''" | payload="'''''''''''",variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9353 | P2 | Injection raw '1; DROP TABLE' | payload='1; DROP TABLE',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9354 | P2 | Injection quoted '1; DROP TABLE' | payload='1; DROP TABLE',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9355 | P2 | Injection html '1; DROP TABLE' | payload='1; DROP TABLE',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9356 | P2 | Injection unicode '1; DROP TABLE' | payload='1; DROP TABLE',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9357 | P2 | Injection raw '../../../etc/passwd' | payload='../../../etc/passwd',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9358 | P2 | Injection quoted '../../../etc/passwd' | payload='../../../etc/passwd',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9359 | P2 | Injection html '../../../etc/passwd' | payload='../../../etc/passwd',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9360 | P2 | Injection unicode '../../../etc/passwd' | payload='../../../etc/passwd',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9361 | P2 | Injection raw 'C:\\boot.ini' | payload='C:\\boot.ini',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9362 | P2 | Injection quoted 'C:\\boot.ini' | payload='C:\\boot.ini',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9363 | P2 | Injection html 'C:\\boot.ini' | payload='C:\\boot.ini',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9364 | P2 | Injection unicode 'C:\\boot.ini' | payload='C:\\boot.ini',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9365 | P2 | Injection raw '<IMG SRC=javascript:' | payload='<IMG SRC=javascript:',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9366 | P2 | Injection quoted '<IMG SRC=javascript:' | payload='<IMG SRC=javascript:',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9367 | P2 | Injection html '<IMG SRC=javascript:' | payload='<IMG SRC=javascript:',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9368 | P2 | Injection unicode '<IMG SRC=javascript:' | payload='<IMG SRC=javascript:',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9369 | P2 | Injection raw '<svg onload=alert(1)' | payload='<svg onload=alert(1)',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9370 | P2 | Injection quoted '<svg onload=alert(1)' | payload='<svg onload=alert(1)',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9371 | P2 | Injection html '<svg onload=alert(1)' | payload='<svg onload=alert(1)',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9372 | P2 | Injection unicode '<svg onload=alert(1)' | payload='<svg onload=alert(1)',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9373 | P2 | Injection raw '<iframe src=evil>' | payload='<iframe src=evil>',variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9374 | P2 | Injection quoted '<iframe src=evil>' | payload='<iframe src=evil>',variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9375 | P2 | Injection html '<iframe src=evil>' | payload='<iframe src=evil>',variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9376 | P2 | Injection unicode '<iframe src=evil>' | payload='<iframe src=evil>',variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9377 | P2 | Injection raw "SELECT 'a' AS b WHER" | payload="SELECT 'a' AS b WHER",variant=raw | moderated | test_security_phase2_part_4.py |
| TC-SEC-9378 | P2 | Injection quoted "SELECT 'a' AS b WHER" | payload="SELECT 'a' AS b WHER",variant=quoted | moderated | test_security_phase2_part_4.py |
| TC-SEC-9379 | P2 | Injection html "SELECT 'a' AS b WHER" | payload="SELECT 'a' AS b WHER",variant=html | moderated | test_security_phase2_part_4.py |
| TC-SEC-9380 | P2 | Injection unicode "SELECT 'a' AS b WHER" | payload="SELECT 'a' AS b WHER",variant=unicode | moderated | test_security_phase2_part_4.py |
| TC-SEC-9381 | P2 | Injection raw 'DROP DATABASE produc' | payload='DROP DATABASE produc',variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9382 | P2 | Injection quoted 'DROP DATABASE produc' | payload='DROP DATABASE produc',variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9383 | P2 | Injection html 'DROP DATABASE produc' | payload='DROP DATABASE produc',variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9384 | P2 | Injection unicode 'DROP DATABASE produc' | payload='DROP DATABASE produc',variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9385 | P2 | Injection raw 'TRUNCATE TABLE logs' | payload='TRUNCATE TABLE logs',variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9386 | P2 | Injection quoted 'TRUNCATE TABLE logs' | payload='TRUNCATE TABLE logs',variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9387 | P2 | Injection html 'TRUNCATE TABLE logs' | payload='TRUNCATE TABLE logs',variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9388 | P2 | Injection unicode 'TRUNCATE TABLE logs' | payload='TRUNCATE TABLE logs',variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9389 | P2 | Injection raw 'REPLACE INTO words V' | payload='REPLACE INTO words V',variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9390 | P2 | Injection quoted 'REPLACE INTO words V' | payload='REPLACE INTO words V',variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9391 | P2 | Injection html 'REPLACE INTO words V' | payload='REPLACE INTO words V',variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9392 | P2 | Injection unicode 'REPLACE INTO words V' | payload='REPLACE INTO words V',variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9393 | P2 | Injection raw 'alert(document.cooki' | payload='alert(document.cooki',variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9394 | P2 | Injection quoted 'alert(document.cooki' | payload='alert(document.cooki',variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9395 | P2 | Injection html 'alert(document.cooki' | payload='alert(document.cooki',variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9396 | P2 | Injection unicode 'alert(document.cooki' | payload='alert(document.cooki',variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9397 | P2 | Injection raw "eval('alert(1)')" | payload="eval('alert(1)')",variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9398 | P2 | Injection quoted "eval('alert(1)')" | payload="eval('alert(1)')",variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9399 | P2 | Injection html "eval('alert(1)')" | payload="eval('alert(1)')",variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9400 | P2 | Injection unicode "eval('alert(1)')" | payload="eval('alert(1)')",variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9401 | P2 | Injection raw "new Function('alert(" | payload="new Function('alert(",variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9402 | P2 | Injection quoted "new Function('alert(" | payload="new Function('alert(",variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9403 | P2 | Injection html "new Function('alert(" | payload="new Function('alert(",variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9404 | P2 | Injection unicode "new Function('alert(" | payload="new Function('alert(",variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9405 | P2 | Injection raw '{% raw %}{% endraw %' | payload='{% raw %}{% endraw %',variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9406 | P2 | Injection quoted '{% raw %}{% endraw %' | payload='{% raw %}{% endraw %',variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9407 | P2 | Injection html '{% raw %}{% endraw %' | payload='{% raw %}{% endraw %',variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9408 | P2 | Injection unicode '{% raw %}{% endraw %' | payload='{% raw %}{% endraw %',variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9409 | P2 | Injection raw '{{config}}' | payload='{{config}}',variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9410 | P2 | Injection quoted '{{config}}' | payload='{{config}}',variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9411 | P2 | Injection html '{{config}}' | payload='{{config}}',variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9412 | P2 | Injection unicode '{{config}}' | payload='{{config}}',variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9413 | P2 | Injection raw '[[$5*5]]' | payload='[[$5*5]]',variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9414 | P2 | Injection quoted '[[$5*5]]' | payload='[[$5*5]]',variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9415 | P2 | Injection html '[[$5*5]]' | payload='[[$5*5]]',variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9416 | P2 | Injection unicode '[[$5*5]]' | payload='[[$5*5]]',variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9417 | P2 | Injection raw '<%= 7*7 %>' | payload='<%= 7*7 %>',variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9418 | P2 | Injection quoted '<%= 7*7 %>' | payload='<%= 7*7 %>',variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9419 | P2 | Injection html '<%= 7*7 %>' | payload='<%= 7*7 %>',variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9420 | P2 | Injection unicode '<%= 7*7 %>' | payload='<%= 7*7 %>',variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9421 | P2 | Injection raw "; sh -c 'rm -rf /'" | payload="; sh -c 'rm -rf /'",variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9422 | P2 | Injection quoted "; sh -c 'rm -rf /'" | payload="; sh -c 'rm -rf /'",variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9423 | P2 | Injection html "; sh -c 'rm -rf /'" | payload="; sh -c 'rm -rf /'",variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9424 | P2 | Injection unicode "; sh -c 'rm -rf /'" | payload="; sh -c 'rm -rf /'",variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9425 | P2 | Injection raw '| cat /etc/shadow' | payload='| cat /etc/shadow',variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9426 | P2 | Injection quoted '| cat /etc/shadow' | payload='| cat /etc/shadow',variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9427 | P2 | Injection html '| cat /etc/shadow' | payload='| cat /etc/shadow',variant=html | moderated | test_security_phase2_part_5.py |
| TC-SEC-9428 | P2 | Injection unicode '| cat /etc/shadow' | payload='| cat /etc/shadow',variant=unicode | moderated | test_security_phase2_part_5.py |
| TC-SEC-9429 | P2 | Injection raw '&& whoami' | payload='&& whoami',variant=raw | moderated | test_security_phase2_part_5.py |
| TC-SEC-9430 | P2 | Injection quoted '&& whoami' | payload='&& whoami',variant=quoted | moderated | test_security_phase2_part_5.py |
| TC-SEC-9449 | P2 | Traversal '../etc/passwd' | payload='../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9450 | P2 | Traversal '../etc/passwd' | payload='../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9451 | P2 | Traversal '../etc/passwd%00' | payload='../etc/passwd%00' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9452 | P2 | Traversal '..%2Fetc%2Fpasswd' | payload='..%2Fetc%2Fpasswd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9453 | P2 | Traversal '..\\windows\\system32' | payload='..\\windows\\system32' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9454 | P2 | Traversal '..%5Cwindows%5Csystem32' | payload='..%5Cwindows%5Csystem32' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9455 | P2 | Traversal '..\\windows\\system32%00' | payload='..\\windows\\system32%00' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9456 | P2 | Traversal '..%5Cwindows%5Csystem32' | payload='..%5Cwindows%5Csystem32' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9457 | P2 | Traversal '%2e%2e%2fetc%2fpasswd' | payload='%2e%2e%2fetc%2fpasswd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9458 | P2 | Traversal '%252e%252e%252fetc%252fp' | payload='%252e%252e%252fetc%252fp' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9459 | P2 | Traversal '%2e%2e%2fetc%2fpasswd%00' | payload='%2e%2e%2fetc%2fpasswd%00' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9460 | P2 | Traversal '%252e%252e%252fetc%252fp' | payload='%252e%252e%252fetc%252fp' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9461 | P2 | Traversal '..%2f..%2fsecret' | payload='..%2f..%2fsecret' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9462 | P2 | Traversal '..%252f..%252fsecret' | payload='..%252f..%252fsecret' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9463 | P2 | Traversal '..%2f..%2fsecret%00' | payload='..%2f..%2fsecret%00' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9464 | P2 | Traversal '..%252f..%252fsecret' | payload='..%252f..%252fsecret' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9465 | P2 | Traversal 'etc/passwd' | payload='etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9466 | P2 | Traversal 'etc/passwd' | payload='etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9467 | P2 | Traversal 'etc/passwd%00' | payload='etc/passwd%00' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9468 | P2 | Traversal 'etc%2Fpasswd' | payload='etc%2Fpasswd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9469 | P2 | Traversal '../../../etc/passwd' | payload='../../../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9470 | P2 | Traversal '../../../etc/passwd' | payload='../../../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9471 | P2 | Traversal '../../../etc/passwd%00' | payload='../../../etc/passwd%00' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9472 | P2 | Traversal '..%2F..%2F..%2Fetc%2Fpas' | payload='..%2F..%2F..%2Fetc%2Fpas' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9473 | P2 | Traversal '....//....//etc/passwd' | payload='....//....//etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9474 | P2 | Traversal '....//....//etc/passwd' | payload='....//....//etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9475 | P2 | Traversal '....//....//etc/passwd%0' | payload='....//....//etc/passwd%0' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9476 | P2 | Traversal '....%2F%2F....%2F%2Fetc%' | payload='....%2F%2F....%2F%2Fetc%' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9477 | P2 | Traversal '..%252f..%252f' | payload='..%252f..%252f' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9478 | P2 | Traversal '..%25252f..%25252f' | payload='..%25252f..%25252f' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9479 | P2 | Traversal '..%252f..%252f%00' | payload='..%252f..%252f%00' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9480 | P2 | Traversal '..%25252f..%25252f' | payload='..%25252f..%25252f' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9481 | P2 | Traversal '..' | payload='..' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9482 | P2 | Traversal '..' | payload='..' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9483 | P2 | Traversal '..%00' | payload='..%00' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9484 | P2 | Traversal '..' | payload='..' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9485 | P2 | Traversal 'a/../../b' | payload='a/../../b' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9486 | P2 | Traversal 'a/../../b' | payload='a/../../b' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9487 | P2 | Traversal 'a/../../b%00' | payload='a/../../b%00' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9488 | P2 | Traversal 'a%2F..%2F..%2Fb' | payload='a%2F..%2F..%2Fb' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9489 | P2 | Traversal '..\\..\\..\\boot.ini' | payload='..\\..\\..\\boot.ini' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9490 | P2 | Traversal '..%5C..%5C..%5Cboot.ini' | payload='..%5C..%5C..%5Cboot.ini' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9491 | P2 | Traversal '..\\..\\..\\boot.ini%00' | payload='..\\..\\..\\boot.ini%00' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9492 | P2 | Traversal '..%5C..%5C..%5Cboot.ini' | payload='..%5C..%5C..%5Cboot.ini' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9493 | P2 | Traversal '..%2f..%2f..%2fetc%2fpas' | payload='..%2f..%2f..%2fetc%2fpas' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9494 | P2 | Traversal '..%252f..%252f..%252fetc' | payload='..%252f..%252f..%252fetc' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9495 | P2 | Traversal '..%2f..%2f..%2fetc%2fpas' | payload='..%2f..%2f..%2fetc%2fpas' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9496 | P2 | Traversal '..%252f..%252f..%252fetc' | payload='..%252f..%252f..%252fetc' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9497 | P2 | Traversal '..././.../etc/passwd' | payload='..././.../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9498 | P2 | Traversal '..././.../etc/passwd' | payload='..././.../etc/passwd' | rejected | test_security_phase2_part_5.py |
| TC-SEC-9501 | P2 | Method POST on /moderate | method=POST,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9502 | P2 | Method GET on /moderate | method=GET,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9503 | P2 | Method PUT on /moderate | method=PUT,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9504 | P2 | Method DELETE on /moderate | method=DELETE,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9505 | P2 | Method PATCH on /moderate | method=PATCH,endpoint=/moderate | restricted | test_security_phase2_part_6.py |
| TC-SEC-9506 | P2 | Method POST on /moderate/batch | method=POST,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9507 | P2 | Method GET on /moderate/batch | method=GET,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9508 | P2 | Method PUT on /moderate/batch | method=PUT,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9509 | P2 | Method DELETE on /moderate/batch | method=DELETE,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9510 | P2 | Method PATCH on /moderate/batch | method=PATCH,endpoint=/moderate/batch | restricted | test_security_phase2_part_6.py |
| TC-SEC-9511 | P2 | Method GET on /health | method=GET,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9512 | P2 | Method POST on /health | method=POST,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9513 | P2 | Method PUT on /health | method=PUT,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9514 | P2 | Method DELETE on /health | method=DELETE,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9515 | P2 | Method PATCH on /health | method=PATCH,endpoint=/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9516 | P2 | Method GET on /metrics | method=GET,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9517 | P2 | Method POST on /metrics | method=POST,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9518 | P2 | Method PUT on /metrics | method=PUT,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9519 | P2 | Method DELETE on /metrics | method=DELETE,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9520 | P2 | Method PATCH on /metrics | method=PATCH,endpoint=/metrics | restricted | test_security_phase2_part_6.py |
| TC-SEC-9521 | P2 | Method GET on / | method=GET,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9522 | P2 | Method POST on / | method=POST,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9523 | P2 | Method PUT on / | method=PUT,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9524 | P2 | Method DELETE on / | method=DELETE,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9525 | P2 | Method PATCH on / | method=PATCH,endpoint=/ | restricted | test_security_phase2_part_6.py |
| TC-SEC-9526 | P2 | Method GET on /admin/wordbank/stats | method=GET,endpoint=/admin/wordbank/stats | restricted | test_security_phase2_part_6.py |
| TC-SEC-9527 | P2 | Method POST on /admin/wordbank/stats | method=POST,endpoint=/admin/wordbank/stats | restricted | test_security_phase2_part_6.py |
| TC-SEC-9528 | P2 | Method PUT on /admin/wordbank/stats | method=PUT,endpoint=/admin/wordbank/stats | restricted | test_security_phase2_part_6.py |
| TC-SEC-9529 | P2 | Method DELETE on /admin/wordbank/stats | method=DELETE,endpoint=/admin/wordbank/stats | restricted | test_security_phase2_part_6.py |
| TC-SEC-9530 | P2 | Method PATCH on /admin/wordbank/stats | method=PATCH,endpoint=/admin/wordbank/stats | restricted | test_security_phase2_part_6.py |
| TC-SEC-9531 | P2 | Method GET on /admin/wordbank/words | method=GET,endpoint=/admin/wordbank/words | restricted | test_security_phase2_part_6.py |
| TC-SEC-9532 | P2 | Method POST on /admin/wordbank/words | method=POST,endpoint=/admin/wordbank/words | restricted | test_security_phase2_part_6.py |
| TC-SEC-9533 | P2 | Method PUT on /admin/wordbank/words | method=PUT,endpoint=/admin/wordbank/words | restricted | test_security_phase2_part_6.py |
| TC-SEC-9534 | P2 | Method DELETE on /admin/wordbank/words | method=DELETE,endpoint=/admin/wordbank/words | restricted | test_security_phase2_part_6.py |
| TC-SEC-9535 | P2 | Method PATCH on /admin/wordbank/words | method=PATCH,endpoint=/admin/wordbank/words | restricted | test_security_phase2_part_6.py |
| TC-SEC-9536 | P2 | Method GET on /admin/wordbank/export | method=GET,endpoint=/admin/wordbank/export | restricted | test_security_phase2_part_6.py |
| TC-SEC-9537 | P2 | Method POST on /admin/wordbank/export | method=POST,endpoint=/admin/wordbank/export | restricted | test_security_phase2_part_6.py |
| TC-SEC-9538 | P2 | Method PUT on /admin/wordbank/export | method=PUT,endpoint=/admin/wordbank/export | restricted | test_security_phase2_part_6.py |
| TC-SEC-9539 | P2 | Method DELETE on /admin/wordbank/export | method=DELETE,endpoint=/admin/wordbank/export | restricted | test_security_phase2_part_6.py |
| TC-SEC-9540 | P2 | Method PATCH on /admin/wordbank/export | method=PATCH,endpoint=/admin/wordbank/export | restricted | test_security_phase2_part_6.py |
| TC-SEC-9541 | P2 | Method GET on /admin/wordbank/languages | method=GET,endpoint=/admin/wordbank/languages | restricted | test_security_phase2_part_6.py |
| TC-SEC-9542 | P2 | Method POST on /admin/wordbank/languages | method=POST,endpoint=/admin/wordbank/languages | restricted | test_security_phase2_part_6.py |
| TC-SEC-9543 | P2 | Method PUT on /admin/wordbank/languages | method=PUT,endpoint=/admin/wordbank/languages | restricted | test_security_phase2_part_6.py |
| TC-SEC-9544 | P2 | Method DELETE on /admin/wordbank/languages | method=DELETE,endpoint=/admin/wordbank/languages | restricted | test_security_phase2_part_6.py |
| TC-SEC-9545 | P2 | Method PATCH on /admin/wordbank/languages | method=PATCH,endpoint=/admin/wordbank/languages | restricted | test_security_phase2_part_6.py |
| TC-SEC-9546 | P2 | Method GET on /admin/wordbank/categories | method=GET,endpoint=/admin/wordbank/categories | restricted | test_security_phase2_part_6.py |
| TC-SEC-9547 | P2 | Method POST on /admin/wordbank/categories | method=POST,endpoint=/admin/wordbank/categories | restricted | test_security_phase2_part_6.py |
| TC-SEC-9548 | P2 | Method PUT on /admin/wordbank/categories | method=PUT,endpoint=/admin/wordbank/categories | restricted | test_security_phase2_part_6.py |
| TC-SEC-9549 | P2 | Method DELETE on /admin/wordbank/categories | method=DELETE,endpoint=/admin/wordbank/categories | restricted | test_security_phase2_part_6.py |
| TC-SEC-9550 | P2 | Method PATCH on /admin/wordbank/categories | method=PATCH,endpoint=/admin/wordbank/categories | restricted | test_security_phase2_part_6.py |
| TC-SEC-9551 | P2 | Method POST on /admin/wordbank/import | method=POST,endpoint=/admin/wordbank/import | restricted | test_security_phase2_part_6.py |
| TC-SEC-9552 | P2 | Method GET on /admin/wordbank/import | method=GET,endpoint=/admin/wordbank/import | restricted | test_security_phase2_part_6.py |
| TC-SEC-9553 | P2 | Method PUT on /admin/wordbank/import | method=PUT,endpoint=/admin/wordbank/import | restricted | test_security_phase2_part_6.py |
| TC-SEC-9554 | P2 | Method DELETE on /admin/wordbank/import | method=DELETE,endpoint=/admin/wordbank/import | restricted | test_security_phase2_part_6.py |
| TC-SEC-9555 | P2 | Method PATCH on /admin/wordbank/import | method=PATCH,endpoint=/admin/wordbank/import | restricted | test_security_phase2_part_6.py |
| TC-SEC-9556 | P2 | Method POST on /admin/reload | method=POST,endpoint=/admin/reload | restricted | test_security_phase2_part_6.py |
| TC-SEC-9557 | P2 | Method GET on /admin/reload | method=GET,endpoint=/admin/reload | restricted | test_security_phase2_part_6.py |
| TC-SEC-9558 | P2 | Method PUT on /admin/reload | method=PUT,endpoint=/admin/reload | restricted | test_security_phase2_part_6.py |
| TC-SEC-9559 | P2 | Method DELETE on /admin/reload | method=DELETE,endpoint=/admin/reload | restricted | test_security_phase2_part_6.py |
| TC-SEC-9560 | P2 | Method PATCH on /admin/reload | method=PATCH,endpoint=/admin/reload | restricted | test_security_phase2_part_6.py |
| TC-SEC-9561 | P2 | Method GET on /admin/app-config | method=GET,endpoint=/admin/app-config | restricted | test_security_phase2_part_6.py |
| TC-SEC-9562 | P2 | Method POST on /admin/app-config | method=POST,endpoint=/admin/app-config | restricted | test_security_phase2_part_6.py |
| TC-SEC-9563 | P2 | Method PUT on /admin/app-config | method=PUT,endpoint=/admin/app-config | restricted | test_security_phase2_part_6.py |
| TC-SEC-9564 | P2 | Method DELETE on /admin/app-config | method=DELETE,endpoint=/admin/app-config | restricted | test_security_phase2_part_6.py |
| TC-SEC-9565 | P2 | Method PATCH on /admin/app-config | method=PATCH,endpoint=/admin/app-config | restricted | test_security_phase2_part_6.py |
| TC-SEC-9566 | P2 | Method GET on /admin/app-config/demo | method=GET,endpoint=/admin/app-config/demo | restricted | test_security_phase2_part_6.py |
| TC-SEC-9567 | P2 | Method POST on /admin/app-config/demo | method=POST,endpoint=/admin/app-config/demo | restricted | test_security_phase2_part_6.py |
| TC-SEC-9568 | P2 | Method PUT on /admin/app-config/demo | method=PUT,endpoint=/admin/app-config/demo | restricted | test_security_phase2_part_6.py |
| TC-SEC-9569 | P2 | Method DELETE on /admin/app-config/demo | method=DELETE,endpoint=/admin/app-config/demo | restricted | test_security_phase2_part_6.py |
| TC-SEC-9570 | P2 | Method PATCH on /admin/app-config/demo | method=PATCH,endpoint=/admin/app-config/demo | restricted | test_security_phase2_part_6.py |
| TC-SEC-9571 | P2 | Method GET on /admin/app-config/other | method=GET,endpoint=/admin/app-config/other | restricted | test_security_phase2_part_6.py |
| TC-SEC-9572 | P2 | Method POST on /admin/app-config/other | method=POST,endpoint=/admin/app-config/other | restricted | test_security_phase2_part_6.py |
| TC-SEC-9573 | P2 | Method PUT on /admin/app-config/other | method=PUT,endpoint=/admin/app-config/other | restricted | test_security_phase2_part_6.py |
| TC-SEC-9574 | P2 | Method DELETE on /admin/app-config/other | method=DELETE,endpoint=/admin/app-config/other | restricted | test_security_phase2_part_6.py |
| TC-SEC-9575 | P2 | Method PATCH on /admin/app-config/other | method=PATCH,endpoint=/admin/app-config/other | restricted | test_security_phase2_part_6.py |
| TC-SEC-9576 | P2 | Method GET on /admin/settings | method=GET,endpoint=/admin/settings | restricted | test_security_phase2_part_6.py |
| TC-SEC-9577 | P2 | Method POST on /admin/settings | method=POST,endpoint=/admin/settings | restricted | test_security_phase2_part_6.py |
| TC-SEC-9578 | P2 | Method PUT on /admin/settings | method=PUT,endpoint=/admin/settings | restricted | test_security_phase2_part_6.py |
| TC-SEC-9579 | P2 | Method DELETE on /admin/settings | method=DELETE,endpoint=/admin/settings | restricted | test_security_phase2_part_6.py |
| TC-SEC-9580 | P2 | Method PATCH on /admin/settings | method=PATCH,endpoint=/admin/settings | restricted | test_security_phase2_part_6.py |
| TC-SEC-9581 | P2 | Method GET on /admin/logs | method=GET,endpoint=/admin/logs | restricted | test_security_phase2_part_6.py |
| TC-SEC-9582 | P2 | Method POST on /admin/logs | method=POST,endpoint=/admin/logs | restricted | test_security_phase2_part_6.py |
| TC-SEC-9583 | P2 | Method PUT on /admin/logs | method=PUT,endpoint=/admin/logs | restricted | test_security_phase2_part_6.py |
| TC-SEC-9584 | P2 | Method DELETE on /admin/logs | method=DELETE,endpoint=/admin/logs | restricted | test_security_phase2_part_6.py |
| TC-SEC-9585 | P2 | Method PATCH on /admin/logs | method=PATCH,endpoint=/admin/logs | restricted | test_security_phase2_part_6.py |
| TC-SEC-9586 | P2 | Method GET on /admin/stats | method=GET,endpoint=/admin/stats | restricted | test_security_phase2_part_6.py |
| TC-SEC-9587 | P2 | Method POST on /admin/stats | method=POST,endpoint=/admin/stats | restricted | test_security_phase2_part_6.py |
| TC-SEC-9588 | P2 | Method PUT on /admin/stats | method=PUT,endpoint=/admin/stats | restricted | test_security_phase2_part_6.py |
| TC-SEC-9589 | P2 | Method DELETE on /admin/stats | method=DELETE,endpoint=/admin/stats | restricted | test_security_phase2_part_6.py |
| TC-SEC-9590 | P2 | Method PATCH on /admin/stats | method=PATCH,endpoint=/admin/stats | restricted | test_security_phase2_part_6.py |
| TC-SEC-9591 | P2 | Method GET on /admin/health | method=GET,endpoint=/admin/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9592 | P2 | Method POST on /admin/health | method=POST,endpoint=/admin/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9593 | P2 | Method PUT on /admin/health | method=PUT,endpoint=/admin/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9594 | P2 | Method DELETE on /admin/health | method=DELETE,endpoint=/admin/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9595 | P2 | Method PATCH on /admin/health | method=PATCH,endpoint=/admin/health | restricted | test_security_phase2_part_6.py |
| TC-SEC-9596 | P2 | Method GET on /admin/spot-check | method=GET,endpoint=/admin/spot-check | restricted | test_security_phase2_part_6.py |
| TC-SEC-9597 | P2 | Method POST on /admin/spot-check | method=POST,endpoint=/admin/spot-check | restricted | test_security_phase2_part_6.py |
| TC-SEC-9598 | P2 | Method PUT on /admin/spot-check | method=PUT,endpoint=/admin/spot-check | restricted | test_security_phase2_part_6.py |
| TC-SEC-9599 | P2 | Method DELETE on /admin/spot-check | method=DELETE,endpoint=/admin/spot-check | restricted | test_security_phase2_part_6.py |
| TC-SEC-9600 | P2 | Method PATCH on /admin/spot-check | method=PATCH,endpoint=/admin/spot-check | restricted | test_security_phase2_part_6.py |
| TC-SEC-9601 | P3 | Encoded payload 0 | variant=0 | safe | test_security_phase2_part_7.py |
| TC-SEC-9602 | P3 | Encoded payload 0 | variant=0 | safe | test_security_phase2_part_7.py |
| TC-SEC-9603 | P3 | Encoded payload 0 | variant=0 | safe | test_security_phase2_part_7.py |
| TC-SEC-9604 | P3 | Encoded payload 0 | variant=0 | safe | test_security_phase2_part_7.py |
| TC-SEC-9605 | P3 | Encoded payload 1 | variant=1 | safe | test_security_phase2_part_7.py |
| TC-SEC-9606 | P3 | Encoded payload 1 | variant=1 | safe | test_security_phase2_part_7.py |
| TC-SEC-9607 | P3 | Encoded payload 1 | variant=1 | safe | test_security_phase2_part_7.py |
| TC-SEC-9608 | P3 | Encoded payload 1 | variant=1 | safe | test_security_phase2_part_7.py |
| TC-SEC-9609 | P3 | Encoded payload 2 | variant=2 | safe | test_security_phase2_part_7.py |
| TC-SEC-9610 | P3 | Encoded payload 2 | variant=2 | safe | test_security_phase2_part_7.py |
| TC-SEC-9611 | P3 | Encoded payload 2 | variant=2 | safe | test_security_phase2_part_7.py |
| TC-SEC-9612 | P3 | Encoded payload 2 | variant=2 | safe | test_security_phase2_part_7.py |
| TC-SEC-9613 | P3 | Encoded payload 3 | variant=3 | safe | test_security_phase2_part_7.py |
| TC-SEC-9614 | P3 | Encoded payload 3 | variant=3 | safe | test_security_phase2_part_7.py |
| TC-SEC-9615 | P3 | Encoded payload 3 | variant=3 | safe | test_security_phase2_part_7.py |
| TC-SEC-9616 | P3 | Encoded payload 3 | variant=3 | safe | test_security_phase2_part_7.py |
| TC-SEC-9617 | P3 | Encoded payload 4 | variant=4 | safe | test_security_phase2_part_7.py |
| TC-SEC-9618 | P3 | Encoded payload 4 | variant=4 | safe | test_security_phase2_part_7.py |
| TC-SEC-9619 | P3 | Encoded payload 4 | variant=4 | safe | test_security_phase2_part_7.py |
| TC-SEC-9620 | P3 | Encoded payload 4 | variant=4 | safe | test_security_phase2_part_7.py |
| TC-SEC-9621 | P3 | Encoded payload 5 | variant=5 | safe | test_security_phase2_part_7.py |
| TC-SEC-9622 | P3 | Encoded payload 5 | variant=5 | safe | test_security_phase2_part_7.py |
| TC-SEC-9623 | P3 | Encoded payload 5 | variant=5 | safe | test_security_phase2_part_7.py |
| TC-SEC-9624 | P3 | Encoded payload 5 | variant=5 | safe | test_security_phase2_part_7.py |
| TC-SEC-9625 | P3 | Encoded payload 6 | variant=6 | safe | test_security_phase2_part_7.py |
| TC-SEC-9626 | P3 | Encoded payload 6 | variant=6 | safe | test_security_phase2_part_7.py |
| TC-SEC-9627 | P3 | Encoded payload 6 | variant=6 | safe | test_security_phase2_part_7.py |
| TC-SEC-9628 | P3 | Encoded payload 6 | variant=6 | safe | test_security_phase2_part_7.py |
| TC-SEC-9629 | P3 | Encoded payload 7 | variant=7 | safe | test_security_phase2_part_7.py |
| TC-SEC-9630 | P3 | Encoded payload 7 | variant=7 | safe | test_security_phase2_part_7.py |
| TC-SEC-9631 | P3 | Encoded payload 7 | variant=7 | safe | test_security_phase2_part_7.py |
| TC-SEC-9632 | P3 | Encoded payload 7 | variant=7 | safe | test_security_phase2_part_7.py |
| TC-SEC-9633 | P3 | Encoded payload 8 | variant=8 | safe | test_security_phase2_part_7.py |
| TC-SEC-9634 | P3 | Encoded payload 8 | variant=8 | safe | test_security_phase2_part_7.py |
| TC-SEC-9635 | P3 | Encoded payload 8 | variant=8 | safe | test_security_phase2_part_7.py |
| TC-SEC-9636 | P3 | Encoded payload 8 | variant=8 | safe | test_security_phase2_part_7.py |
| TC-SEC-9637 | P3 | Encoded payload 9 | variant=9 | safe | test_security_phase2_part_7.py |
| TC-SEC-9638 | P3 | Encoded payload 9 | variant=9 | safe | test_security_phase2_part_7.py |
| TC-SEC-9639 | P3 | Encoded payload 9 | variant=9 | safe | test_security_phase2_part_7.py |
| TC-SEC-9640 | P3 | Encoded payload 9 | variant=9 | safe | test_security_phase2_part_7.py |
| TC-SEC-9641 | P3 | Encoded payload 10 | variant=10 | safe | test_security_phase2_part_7.py |
| TC-SEC-9642 | P3 | Encoded payload 10 | variant=10 | safe | test_security_phase2_part_7.py |
| TC-SEC-9643 | P3 | Encoded payload 10 | variant=10 | safe | test_security_phase2_part_7.py |
| TC-SEC-9644 | P3 | Encoded payload 10 | variant=10 | safe | test_security_phase2_part_7.py |
| TC-SEC-9645 | P3 | Encoded payload 11 | variant=11 | safe | test_security_phase2_part_7.py |
| TC-SEC-9646 | P3 | Encoded payload 11 | variant=11 | safe | test_security_phase2_part_7.py |
| TC-SEC-9647 | P3 | Encoded payload 11 | variant=11 | safe | test_security_phase2_part_7.py |
| TC-SEC-9648 | P3 | Encoded payload 11 | variant=11 | safe | test_security_phase2_part_7.py |
| TC-SEC-9649 | P3 | Encoded payload 12 | variant=12 | safe | test_security_phase2_part_7.py |
| TC-SEC-9650 | P3 | Encoded payload 12 | variant=12 | safe | test_security_phase2_part_7.py |
| TC-SEC-9651 | P3 | Encoded payload 12 | variant=12 | safe | test_security_phase2_part_7.py |
| TC-SEC-9652 | P3 | Encoded payload 12 | variant=12 | safe | test_security_phase2_part_7.py |
| TC-SEC-9653 | P3 | Encoded payload 13 | variant=13 | safe | test_security_phase2_part_7.py |
| TC-SEC-9654 | P3 | Encoded payload 13 | variant=13 | safe | test_security_phase2_part_7.py |
| TC-SEC-9655 | P3 | Encoded payload 13 | variant=13 | safe | test_security_phase2_part_7.py |
| TC-SEC-9656 | P3 | Encoded payload 13 | variant=13 | safe | test_security_phase2_part_7.py |
| TC-SEC-9657 | P3 | Encoded payload 14 | variant=14 | safe | test_security_phase2_part_7.py |
| TC-SEC-9658 | P3 | Encoded payload 14 | variant=14 | safe | test_security_phase2_part_7.py |
| TC-SEC-9659 | P3 | Encoded payload 14 | variant=14 | safe | test_security_phase2_part_7.py |
| TC-SEC-9660 | P3 | Encoded payload 14 | variant=14 | safe | test_security_phase2_part_7.py |
| TC-SEC-9661 | P3 | Encoded payload 15 | variant=15 | safe | test_security_phase2_part_7.py |
| TC-SEC-9662 | P3 | Encoded payload 15 | variant=15 | safe | test_security_phase2_part_7.py |
| TC-SEC-9663 | P3 | Encoded payload 15 | variant=15 | safe | test_security_phase2_part_7.py |
| TC-SEC-9664 | P3 | Encoded payload 15 | variant=15 | safe | test_security_phase2_part_7.py |
| TC-SEC-9665 | P3 | Encoded payload 16 | variant=16 | safe | test_security_phase2_part_7.py |
| TC-SEC-9666 | P3 | Encoded payload 16 | variant=16 | safe | test_security_phase2_part_7.py |
| TC-SEC-9667 | P3 | Encoded payload 16 | variant=16 | safe | test_security_phase2_part_7.py |
| TC-SEC-9668 | P3 | Encoded payload 16 | variant=16 | safe | test_security_phase2_part_7.py |
| TC-SEC-9669 | P3 | Encoded payload 17 | variant=17 | safe | test_security_phase2_part_7.py |
| TC-SEC-9670 | P3 | Encoded payload 17 | variant=17 | safe | test_security_phase2_part_7.py |
| TC-SEC-9671 | P3 | Encoded payload 17 | variant=17 | safe | test_security_phase2_part_7.py |
| TC-SEC-9672 | P3 | Encoded payload 17 | variant=17 | safe | test_security_phase2_part_7.py |
| TC-SEC-9673 | P3 | Encoded payload 18 | variant=18 | safe | test_security_phase2_part_7.py |
| TC-SEC-9674 | P3 | Encoded payload 18 | variant=18 | safe | test_security_phase2_part_7.py |
| TC-SEC-9675 | P3 | Encoded payload 18 | variant=18 | safe | test_security_phase2_part_7.py |
| TC-SEC-9676 | P3 | Encoded payload 18 | variant=18 | safe | test_security_phase2_part_7.py |
| TC-SEC-9677 | P3 | Encoded payload 19 | variant=19 | safe | test_security_phase2_part_7.py |
| TC-SEC-9678 | P3 | Encoded payload 19 | variant=19 | safe | test_security_phase2_part_7.py |
| TC-SEC-9679 | P3 | Encoded payload 19 | variant=19 | safe | test_security_phase2_part_7.py |
| TC-SEC-9680 | P3 | Encoded payload 19 | variant=19 | safe | test_security_phase2_part_7.py |
| TC-SEC-9681 | P3 | Encoded payload 20 | variant=20 | safe | test_security_phase2_part_7.py |
| TC-SEC-9682 | P3 | Encoded payload 20 | variant=20 | safe | test_security_phase2_part_7.py |
| TC-SEC-9683 | P3 | Encoded payload 20 | variant=20 | safe | test_security_phase2_part_7.py |
| TC-SEC-9684 | P3 | Encoded payload 20 | variant=20 | safe | test_security_phase2_part_7.py |
| TC-SEC-9685 | P3 | Encoded payload 21 | variant=21 | safe | test_security_phase2_part_7.py |
| TC-SEC-9686 | P3 | Encoded payload 21 | variant=21 | safe | test_security_phase2_part_7.py |
| TC-SEC-9687 | P3 | Encoded payload 21 | variant=21 | safe | test_security_phase2_part_7.py |
| TC-SEC-9688 | P3 | Encoded payload 21 | variant=21 | safe | test_security_phase2_part_7.py |
| TC-SEC-9689 | P3 | Encoded payload 22 | variant=22 | safe | test_security_phase2_part_7.py |
| TC-SEC-9690 | P3 | Encoded payload 22 | variant=22 | safe | test_security_phase2_part_7.py |
| TC-SEC-9691 | P3 | Encoded payload 22 | variant=22 | safe | test_security_phase2_part_7.py |
| TC-SEC-9692 | P3 | Encoded payload 22 | variant=22 | safe | test_security_phase2_part_7.py |
| TC-SEC-9693 | P3 | Encoded payload 23 | variant=23 | safe | test_security_phase2_part_7.py |
| TC-SEC-9694 | P3 | Encoded payload 23 | variant=23 | safe | test_security_phase2_part_7.py |
| TC-SEC-9695 | P3 | Encoded payload 23 | variant=23 | safe | test_security_phase2_part_7.py |
| TC-SEC-9696 | P3 | Encoded payload 23 | variant=23 | safe | test_security_phase2_part_7.py |
| TC-SEC-9697 | P3 | Encoded payload 24 | variant=24 | safe | test_security_phase2_part_7.py |
| TC-SEC-9698 | P3 | Encoded payload 24 | variant=24 | safe | test_security_phase2_part_7.py |
| TC-SEC-9699 | P3 | Encoded payload 24 | variant=24 | safe | test_security_phase2_part_7.py |
| TC-SEC-9700 | P3 | Encoded payload 24 | variant=24 | safe | test_security_phase2_part_7.py |

### Phase 3 - 20,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-SEC-0781 onward.

### Phase 4 - 200,000 cases
- Planned high-scale scenarios, IDs TC-SEC-20781 onward.

### Phase 5 - 1,779,220 cases
- Planned exhaustive dimension sweep, IDs TC-SEC-220781 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_security_phase2_part_1.py | 8931-9030 | P1 | :white_check_mark: Phase 2 |
| test_security_phase2_part_2.py | 9051-9150 | P1 | :white_check_mark: Phase 2 |
| test_security_phase2_part_3.py | 9171-9270 | P1 | :white_check_mark: Phase 2 |
| test_security_phase2_part_4.py | 9281-9380 | P2 | :white_check_mark: Phase 2 |
| test_security_phase2_part_5.py | 9381-9498 | P2 | :white_check_mark: Phase 2 |
| test_security_phase2_part_6.py | 9501-9600 | P2 | :white_check_mark: Phase 2 |
| test_security_phase2_part_7.py | 9601-9700 | P3 | :white_check_mark: Phase 2 |

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
