# Model/LLM Module Test Documentation

## Overview
- **Total Planned:** 900,000
- **Phase 1:** 60 (IDs TC-MODEL-001 to TC-MODEL-0060) :white_check_mark: Implemented
- **Phase 2:** 550 (IDs TC-MODEL-0061 to TC-MODEL-0610) :white_check_mark: Implemented
- **Phase 3:** 10,000 (IDs TC-MODEL-0611 to TC-MODEL-10610) :hourglass: Planned
- **Phase 4:** 100,000 (IDs TC-MODEL-10611 to TC-MODEL-110610) :hourglass: Planned
- **Phase 5:** 789,390 (IDs TC-MODEL-110611 to TC-MODEL-900000) :hourglass: Planned

## Dimension Matrix
| Dimension | Values (Phase 2) |
| :--- | :--- |
| Model state | missing, local, downloading |
| Endpoint | primary, mirror, modelscope, none |
| Retry count | 0-3 |
| Prompt injection | control tokens, XML, prefixes |
| Cache type | q8_0, f16, q4_0, q4_1, q5_0, q5_1, q2_k, f32 |
| Threads | auto, numeric |

## Test Case List

### Phase 1 - 60 cases
- 60 cases (sanitize, download, retry).

### Phase 2 (Current) - 550 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-MODEL-5013 | P1 | Sanitize #0 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5014 | P1 | Sanitize #1 (absent) | mode=absent,marker='<|im_end|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5015 | P1 | Sanitize #2 (absent) | mode=absent,marker='<|endoftext|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5016 | P1 | Sanitize #3 (absent) | mode=absent,marker='<|endofmask|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5017 | P1 | Sanitize #4 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5018 | P1 | Sanitize #5 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5019 | P1 | Sanitize #6 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5020 | P1 | Sanitize #7 (absent) | mode=absent,marker='system:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5021 | P1 | Sanitize #8 (absent) | mode=absent,marker='user:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5022 | P1 | Sanitize #9 (absent) | mode=absent,marker='assistant:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5023 | P1 | Sanitize #10 (absent) | mode=absent,marker='System:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5024 | P1 | Sanitize #11 (equal) | mode=equal,marker='&lt;script&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5025 | P1 | Sanitize #12 (equal) | mode=equal,marker='&lt;b&gt;bold&lt;/b&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5026 | P1 | Sanitize #13 (equal) | mode=equal,marker='&lt;i&gt;italic&lt;/i&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5027 | P1 | Sanitize #14 (equal) | mode=equal,marker='a &lt; b' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5028 | P1 | Sanitize #15 (equal) | mode=equal,marker='1 &gt; 0' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5029 | P1 | Sanitize #16 (equal) | mode=equal,marker='a &amp; b' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5030 | P1 | Sanitize #17 (equal) | mode=equal,marker='say &quot;hi&quot;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5031 | P1 | Sanitize #18 (equal) | mode=equal,marker='&lt;img src=x&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5032 | P1 | Sanitize #19 (equal) | mode=equal,marker='&lt;a href=evil&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5033 | P1 | Sanitize #20 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5034 | P1 | Sanitize #21 (absent) | mode=absent,marker='<|im_end|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5035 | P1 | Sanitize #22 (absent) | mode=absent,marker='<|endoftext|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5036 | P1 | Sanitize #23 (absent) | mode=absent,marker='<|endofmask|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5037 | P1 | Sanitize #24 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5038 | P1 | Sanitize #25 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5039 | P1 | Sanitize #26 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5040 | P1 | Sanitize #27 (absent) | mode=absent,marker='system:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5041 | P1 | Sanitize #28 (absent) | mode=absent,marker='user:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5042 | P1 | Sanitize #29 (absent) | mode=absent,marker='assistant:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5043 | P1 | Sanitize #30 (absent) | mode=absent,marker='System:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5044 | P1 | Sanitize #31 (equal) | mode=equal,marker='&lt;script&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5045 | P1 | Sanitize #32 (equal) | mode=equal,marker='&lt;b&gt;bold&lt;/b&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5046 | P1 | Sanitize #33 (equal) | mode=equal,marker='&lt;i&gt;italic&lt;/i&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5047 | P1 | Sanitize #34 (equal) | mode=equal,marker='a &lt; b' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5048 | P1 | Sanitize #35 (equal) | mode=equal,marker='1 &gt; 0' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5049 | P1 | Sanitize #36 (equal) | mode=equal,marker='a &amp; b' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5050 | P1 | Sanitize #37 (equal) | mode=equal,marker='say &quot;hi&quot;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5051 | P1 | Sanitize #38 (equal) | mode=equal,marker='&lt;img src=x&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5052 | P1 | Sanitize #39 (equal) | mode=equal,marker='&lt;a href=evil&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5053 | P1 | Sanitize #40 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5054 | P1 | Sanitize #41 (absent) | mode=absent,marker='<|im_end|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5055 | P1 | Sanitize #42 (absent) | mode=absent,marker='<|endoftext|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5056 | P1 | Sanitize #43 (absent) | mode=absent,marker='<|endofmask|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5057 | P1 | Sanitize #44 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5058 | P1 | Sanitize #45 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5059 | P1 | Sanitize #46 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5060 | P1 | Sanitize #47 (absent) | mode=absent,marker='system:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5061 | P1 | Sanitize #48 (absent) | mode=absent,marker='user:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5062 | P1 | Sanitize #49 (absent) | mode=absent,marker='assistant:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5063 | P1 | Sanitize #50 (absent) | mode=absent,marker='System:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5064 | P1 | Sanitize #51 (equal) | mode=equal,marker='&lt;script&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5065 | P1 | Sanitize #52 (equal) | mode=equal,marker='&lt;b&gt;bold&lt;/b&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5066 | P1 | Sanitize #53 (equal) | mode=equal,marker='&lt;i&gt;italic&lt;/i&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5067 | P1 | Sanitize #54 (equal) | mode=equal,marker='a &lt; b' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5068 | P1 | Sanitize #55 (equal) | mode=equal,marker='1 &gt; 0' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5069 | P1 | Sanitize #56 (equal) | mode=equal,marker='a &amp; b' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5070 | P1 | Sanitize #57 (equal) | mode=equal,marker='say &quot;hi&quot;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5071 | P1 | Sanitize #58 (equal) | mode=equal,marker='&lt;img src=x&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5072 | P1 | Sanitize #59 (equal) | mode=equal,marker='&lt;a href=evil&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5073 | P1 | Sanitize #60 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5074 | P1 | Sanitize #61 (absent) | mode=absent,marker='<|im_end|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5075 | P1 | Sanitize #62 (absent) | mode=absent,marker='<|endoftext|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5076 | P1 | Sanitize #63 (absent) | mode=absent,marker='<|endofmask|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5077 | P1 | Sanitize #64 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5078 | P1 | Sanitize #65 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5079 | P1 | Sanitize #66 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5080 | P1 | Sanitize #67 (absent) | mode=absent,marker='system:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5081 | P1 | Sanitize #68 (absent) | mode=absent,marker='user:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5082 | P1 | Sanitize #69 (absent) | mode=absent,marker='assistant:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5083 | P1 | Sanitize #70 (absent) | mode=absent,marker='System:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5084 | P1 | Sanitize #71 (equal) | mode=equal,marker='&lt;script&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5085 | P1 | Sanitize #72 (equal) | mode=equal,marker='&lt;b&gt;bold&lt;/b&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5086 | P1 | Sanitize #73 (equal) | mode=equal,marker='&lt;i&gt;italic&lt;/i&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5087 | P1 | Sanitize #74 (equal) | mode=equal,marker='a &lt; b' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5088 | P1 | Sanitize #75 (equal) | mode=equal,marker='1 &gt; 0' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5089 | P1 | Sanitize #76 (equal) | mode=equal,marker='a &amp; b' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5090 | P1 | Sanitize #77 (equal) | mode=equal,marker='say &quot;hi&quot;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5091 | P1 | Sanitize #78 (equal) | mode=equal,marker='&lt;img src=x&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5092 | P1 | Sanitize #79 (equal) | mode=equal,marker='&lt;a href=evil&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5093 | P1 | Sanitize #80 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5094 | P1 | Sanitize #81 (absent) | mode=absent,marker='<|im_end|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5095 | P1 | Sanitize #82 (absent) | mode=absent,marker='<|endoftext|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5096 | P1 | Sanitize #83 (absent) | mode=absent,marker='<|endofmask|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5097 | P1 | Sanitize #84 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5098 | P1 | Sanitize #85 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5099 | P1 | Sanitize #86 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5100 | P1 | Sanitize #87 (absent) | mode=absent,marker='system:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5101 | P1 | Sanitize #88 (absent) | mode=absent,marker='user:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5102 | P1 | Sanitize #89 (absent) | mode=absent,marker='assistant:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5103 | P1 | Sanitize #90 (absent) | mode=absent,marker='System:' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5104 | P1 | Sanitize #91 (equal) | mode=equal,marker='&lt;script&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5105 | P1 | Sanitize #92 (equal) | mode=equal,marker='&lt;b&gt;bold&lt;/b&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5106 | P1 | Sanitize #93 (equal) | mode=equal,marker='&lt;i&gt;italic&lt;/i&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5107 | P1 | Sanitize #94 (equal) | mode=equal,marker='a &lt; b' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5108 | P1 | Sanitize #95 (equal) | mode=equal,marker='1 &gt; 0' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5109 | P1 | Sanitize #96 (equal) | mode=equal,marker='a &amp; b' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5110 | P1 | Sanitize #97 (equal) | mode=equal,marker='say &quot;hi&quot;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5111 | P1 | Sanitize #98 (equal) | mode=equal,marker='&lt;img src=x&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5112 | P1 | Sanitize #99 (equal) | mode=equal,marker='&lt;a href=evil&gt;' | sanitized | test_model_phase2_part_1.py |
| TC-MODEL-5113 | P1 | Sanitize #100 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5114 | P1 | Sanitize #101 (absent) | mode=absent,marker='<|im_end|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5115 | P1 | Sanitize #102 (absent) | mode=absent,marker='<|endoftext|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5116 | P1 | Sanitize #103 (absent) | mode=absent,marker='<|endofmask|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5117 | P1 | Sanitize #104 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5118 | P1 | Sanitize #105 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5119 | P1 | Sanitize #106 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5120 | P1 | Sanitize #107 (absent) | mode=absent,marker='system:' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5121 | P1 | Sanitize #108 (absent) | mode=absent,marker='user:' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5122 | P1 | Sanitize #109 (absent) | mode=absent,marker='assistant:' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5123 | P1 | Sanitize #110 (absent) | mode=absent,marker='System:' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5124 | P1 | Sanitize #111 (equal) | mode=equal,marker='&lt;script&gt;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5125 | P1 | Sanitize #112 (equal) | mode=equal,marker='&lt;b&gt;bold&lt;/b&gt;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5126 | P1 | Sanitize #113 (equal) | mode=equal,marker='&lt;i&gt;italic&lt;/i&gt;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5127 | P1 | Sanitize #114 (equal) | mode=equal,marker='a &lt; b' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5128 | P1 | Sanitize #115 (equal) | mode=equal,marker='1 &gt; 0' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5129 | P1 | Sanitize #116 (equal) | mode=equal,marker='a &amp; b' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5130 | P1 | Sanitize #117 (equal) | mode=equal,marker='say &quot;hi&quot;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5131 | P1 | Sanitize #118 (equal) | mode=equal,marker='&lt;img src=x&gt;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5132 | P1 | Sanitize #119 (equal) | mode=equal,marker='&lt;a href=evil&gt;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5133 | P1 | Sanitize #120 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5134 | P1 | Sanitize #121 (absent) | mode=absent,marker='<|im_end|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5135 | P1 | Sanitize #122 (absent) | mode=absent,marker='<|endoftext|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5136 | P1 | Sanitize #123 (absent) | mode=absent,marker='<|endofmask|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5137 | P1 | Sanitize #124 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5138 | P1 | Sanitize #125 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5139 | P1 | Sanitize #126 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5140 | P1 | Sanitize #127 (absent) | mode=absent,marker='system:' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5141 | P1 | Sanitize #128 (absent) | mode=absent,marker='user:' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5142 | P1 | Sanitize #129 (absent) | mode=absent,marker='assistant:' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5143 | P1 | Sanitize #130 (absent) | mode=absent,marker='System:' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5144 | P1 | Sanitize #131 (equal) | mode=equal,marker='&lt;script&gt;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5145 | P1 | Sanitize #132 (equal) | mode=equal,marker='&lt;b&gt;bold&lt;/b&gt;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5146 | P1 | Sanitize #133 (equal) | mode=equal,marker='&lt;i&gt;italic&lt;/i&gt;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5147 | P1 | Sanitize #134 (equal) | mode=equal,marker='a &lt; b' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5148 | P1 | Sanitize #135 (equal) | mode=equal,marker='1 &gt; 0' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5149 | P1 | Sanitize #136 (equal) | mode=equal,marker='a &amp; b' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5150 | P1 | Sanitize #137 (equal) | mode=equal,marker='say &quot;hi&quot;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5151 | P1 | Sanitize #138 (equal) | mode=equal,marker='&lt;img src=x&gt;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5152 | P1 | Sanitize #139 (equal) | mode=equal,marker='&lt;a href=evil&gt;' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5153 | P1 | Sanitize #140 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5154 | P1 | Sanitize #141 (absent) | mode=absent,marker='<|im_end|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5155 | P1 | Sanitize #142 (absent) | mode=absent,marker='<|endoftext|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5156 | P1 | Sanitize #143 (absent) | mode=absent,marker='<|endofmask|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5157 | P1 | Sanitize #144 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5158 | P1 | Sanitize #145 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5159 | P1 | Sanitize #146 (absent) | mode=absent,marker='<|im_start|>' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5160 | P1 | Sanitize #147 (absent) | mode=absent,marker='system:' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5161 | P1 | Sanitize #148 (absent) | mode=absent,marker='user:' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5162 | P1 | Sanitize #149 (absent) | mode=absent,marker='assistant:' | sanitized | test_model_phase2_part_2.py |
| TC-MODEL-5163 | P1 | Threads auto | configured=auto | valid | test_model_phase2_part_2.py |
| TC-MODEL-5164 | P1 | Threads 0 | configured=0 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5165 | P1 | Threads -1 | configured=-1 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5166 | P1 | Threads abc | configured=abc | valid | test_model_phase2_part_2.py |
| TC-MODEL-5167 | P1 | Threads 1 | configured=1 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5168 | P1 | Threads 2 | configured=2 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5169 | P1 | Threads 3 | configured=3 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5170 | P1 | Threads 4 | configured=4 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5171 | P1 | Threads 5 | configured=5 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5172 | P1 | Threads 6 | configured=6 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5173 | P1 | Threads 7 | configured=7 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5174 | P1 | Threads 8 | configured=8 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5175 | P1 | Threads 9 | configured=9 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5176 | P1 | Threads 10 | configured=10 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5177 | P1 | Threads 11 | configured=11 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5178 | P1 | Threads 12 | configured=12 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5179 | P1 | Threads 13 | configured=13 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5180 | P1 | Threads 14 | configured=14 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5181 | P1 | Threads 15 | configured=15 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5182 | P1 | Threads 16 | configured=16 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5183 | P1 | Threads 17 | configured=17 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5184 | P1 | Threads 18 | configured=18 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5185 | P1 | Threads 19 | configured=19 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5186 | P1 | Threads 20 | configured=20 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5187 | P1 | Threads 21 | configured=21 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5188 | P1 | Threads 22 | configured=22 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5189 | P1 | Threads 23 | configured=23 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5190 | P1 | Threads 24 | configured=24 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5191 | P1 | Threads 25 | configured=25 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5192 | P1 | Threads 26 | configured=26 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5193 | P1 | Threads 27 | configured=27 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5194 | P1 | Threads 28 | configured=28 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5195 | P1 | Threads 29 | configured=29 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5196 | P1 | Threads 30 | configured=30 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5197 | P1 | Threads 31 | configured=31 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5198 | P1 | Threads 32 | configured=32 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5199 | P1 | Threads 33 | configured=33 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5200 | P1 | Threads 34 | configured=34 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5201 | P1 | Threads 35 | configured=35 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5202 | P1 | Threads 36 | configured=36 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5203 | P1 | Threads 37 | configured=37 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5204 | P1 | Threads 38 | configured=38 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5205 | P1 | Threads 39 | configured=39 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5206 | P1 | Threads 40 | configured=40 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5207 | P1 | Threads 41 | configured=41 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5208 | P1 | Threads 42 | configured=42 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5209 | P1 | Threads 43 | configured=43 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5210 | P1 | Threads 44 | configured=44 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5211 | P1 | Threads 45 | configured=45 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5212 | P1 | Threads 46 | configured=46 | valid | test_model_phase2_part_2.py |
| TC-MODEL-5213 | P2 | KV cache 'q8_0' | raw='q8_0' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5214 | P2 | KV cache 'Q8_0' | raw='Q8_0' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5215 | P2 | KV cache ' q8_0 ' | raw=' q8_0 ' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5216 | P2 | KV cache 'q8-0' | raw='q8-0' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5217 | P2 | KV cache 'q8_0 ' | raw='q8_0 ' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5218 | P2 | KV cache 'f16' | raw='f16' | enum=15 | test_model_phase2_part_3.py |
| TC-MODEL-5219 | P2 | KV cache 'F16' | raw='F16' | enum=15 | test_model_phase2_part_3.py |
| TC-MODEL-5220 | P2 | KV cache ' f16 ' | raw=' f16 ' | enum=15 | test_model_phase2_part_3.py |
| TC-MODEL-5221 | P2 | KV cache 'f16' | raw='f16' | enum=15 | test_model_phase2_part_3.py |
| TC-MODEL-5222 | P2 | KV cache 'f16 ' | raw='f16 ' | enum=15 | test_model_phase2_part_3.py |
| TC-MODEL-5223 | P2 | KV cache 'q4_0' | raw='q4_0' | enum=2 | test_model_phase2_part_3.py |
| TC-MODEL-5224 | P2 | KV cache 'Q4_0' | raw='Q4_0' | enum=2 | test_model_phase2_part_3.py |
| TC-MODEL-5225 | P2 | KV cache ' q4_0 ' | raw=' q4_0 ' | enum=2 | test_model_phase2_part_3.py |
| TC-MODEL-5226 | P2 | KV cache 'q4-0' | raw='q4-0' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5227 | P2 | KV cache 'q4_0 ' | raw='q4_0 ' | enum=2 | test_model_phase2_part_3.py |
| TC-MODEL-5228 | P2 | KV cache 'q4_1' | raw='q4_1' | enum=3 | test_model_phase2_part_3.py |
| TC-MODEL-5229 | P2 | KV cache 'Q4_1' | raw='Q4_1' | enum=3 | test_model_phase2_part_3.py |
| TC-MODEL-5230 | P2 | KV cache ' q4_1 ' | raw=' q4_1 ' | enum=3 | test_model_phase2_part_3.py |
| TC-MODEL-5231 | P2 | KV cache 'q4-1' | raw='q4-1' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5232 | P2 | KV cache 'q4_1 ' | raw='q4_1 ' | enum=3 | test_model_phase2_part_3.py |
| TC-MODEL-5233 | P2 | KV cache 'q5_0' | raw='q5_0' | enum=8 | test_model_phase2_part_3.py |
| TC-MODEL-5234 | P2 | KV cache 'Q5_0' | raw='Q5_0' | enum=8 | test_model_phase2_part_3.py |
| TC-MODEL-5235 | P2 | KV cache ' q5_0 ' | raw=' q5_0 ' | enum=8 | test_model_phase2_part_3.py |
| TC-MODEL-5236 | P2 | KV cache 'q5-0' | raw='q5-0' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5237 | P2 | KV cache 'q5_0 ' | raw='q5_0 ' | enum=8 | test_model_phase2_part_3.py |
| TC-MODEL-5238 | P2 | KV cache 'q5_1' | raw='q5_1' | enum=9 | test_model_phase2_part_3.py |
| TC-MODEL-5239 | P2 | KV cache 'Q5_1' | raw='Q5_1' | enum=9 | test_model_phase2_part_3.py |
| TC-MODEL-5240 | P2 | KV cache ' q5_1 ' | raw=' q5_1 ' | enum=9 | test_model_phase2_part_3.py |
| TC-MODEL-5241 | P2 | KV cache 'q5-1' | raw='q5-1' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5242 | P2 | KV cache 'q5_1 ' | raw='q5_1 ' | enum=9 | test_model_phase2_part_3.py |
| TC-MODEL-5243 | P2 | KV cache 'q2_k' | raw='q2_k' | enum=10 | test_model_phase2_part_3.py |
| TC-MODEL-5244 | P2 | KV cache 'Q2_K' | raw='Q2_K' | enum=10 | test_model_phase2_part_3.py |
| TC-MODEL-5245 | P2 | KV cache ' q2_k ' | raw=' q2_k ' | enum=10 | test_model_phase2_part_3.py |
| TC-MODEL-5246 | P2 | KV cache 'q2-k' | raw='q2-k' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5247 | P2 | KV cache 'q2_k ' | raw='q2_k ' | enum=10 | test_model_phase2_part_3.py |
| TC-MODEL-5248 | P2 | KV cache 'f32' | raw='f32' | enum=0 | test_model_phase2_part_3.py |
| TC-MODEL-5249 | P2 | KV cache 'F32' | raw='F32' | enum=0 | test_model_phase2_part_3.py |
| TC-MODEL-5250 | P2 | KV cache ' f32 ' | raw=' f32 ' | enum=0 | test_model_phase2_part_3.py |
| TC-MODEL-5251 | P2 | KV cache 'f32' | raw='f32' | enum=0 | test_model_phase2_part_3.py |
| TC-MODEL-5252 | P2 | KV cache 'f32 ' | raw='f32 ' | enum=0 | test_model_phase2_part_3.py |
| TC-MODEL-5253 | P2 | KV cache 'q3_0' | raw='q3_0' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5254 | P2 | KV cache 'q6_0' | raw='q6_0' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5255 | P2 | KV cache 'q3_k' | raw='q3_k' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5256 | P2 | KV cache 'auto' | raw='auto' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5257 | P2 | KV cache 'unknown' | raw='unknown' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5258 | P2 | KV cache 'Q4_2' | raw='Q4_2' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5259 | P2 | KV cache 'f64' | raw='f64' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5260 | P2 | KV cache 'i8' | raw='i8' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5261 | P2 | KV cache 'nf4' | raw='nf4' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5262 | P2 | KV cache 'q8' | raw='q8' | enum=7 | test_model_phase2_part_3.py |
| TC-MODEL-5263 | P2 | Download retry after 0 failures via 0 | failures=0,endpoint=0 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5264 | P2 | Download retry after 0 failures via 1 | failures=0,endpoint=1 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5265 | P2 | Download retry after 0 failures via 2 | failures=0,endpoint=2 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5266 | P2 | Download retry after 0 failures via 3 | failures=0,endpoint=3 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5267 | P2 | Download retry after 0 failures via 4 | failures=0,endpoint=4 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5268 | P2 | Download retry after 0 failures via 5 | failures=0,endpoint=5 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5269 | P2 | Download retry after 0 failures via 6 | failures=0,endpoint=6 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5270 | P2 | Download retry after 0 failures via 7 | failures=0,endpoint=7 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5271 | P2 | Download retry after 0 failures via 8 | failures=0,endpoint=8 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5272 | P2 | Download retry after 0 failures via 9 | failures=0,endpoint=9 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5273 | P2 | Download retry after 0 failures via 10 | failures=0,endpoint=10 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5274 | P2 | Download retry after 0 failures via 11 | failures=0,endpoint=11 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5275 | P2 | Download retry after 0 failures via 12 | failures=0,endpoint=12 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5276 | P2 | Download retry after 0 failures via 13 | failures=0,endpoint=13 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5277 | P2 | Download retry after 0 failures via 14 | failures=0,endpoint=14 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5278 | P2 | Download retry after 0 failures via 15 | failures=0,endpoint=15 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5279 | P2 | Download retry after 0 failures via 16 | failures=0,endpoint=16 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5280 | P2 | Download retry after 0 failures via 17 | failures=0,endpoint=17 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5281 | P2 | Download retry after 0 failures via 18 | failures=0,endpoint=18 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5282 | P2 | Download retry after 0 failures via 19 | failures=0,endpoint=19 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5283 | P2 | Download retry after 0 failures via 20 | failures=0,endpoint=20 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5284 | P2 | Download retry after 0 failures via 21 | failures=0,endpoint=21 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5285 | P2 | Download retry after 0 failures via 22 | failures=0,endpoint=22 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5286 | P2 | Download retry after 0 failures via 23 | failures=0,endpoint=23 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5287 | P2 | Download retry after 0 failures via 24 | failures=0,endpoint=24 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5288 | P2 | Download retry after 0 failures via 25 | failures=0,endpoint=25 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5289 | P2 | Download retry after 0 failures via 26 | failures=0,endpoint=26 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5290 | P2 | Download retry after 0 failures via 27 | failures=0,endpoint=27 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5291 | P2 | Download retry after 0 failures via 28 | failures=0,endpoint=28 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5292 | P2 | Download retry after 0 failures via 29 | failures=0,endpoint=29 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5293 | P2 | Download retry after 0 failures via 30 | failures=0,endpoint=30 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5294 | P2 | Download retry after 0 failures via 31 | failures=0,endpoint=31 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5295 | P2 | Download retry after 0 failures via 32 | failures=0,endpoint=32 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5296 | P2 | Download retry after 0 failures via 33 | failures=0,endpoint=33 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5297 | P2 | Download retry after 0 failures via 34 | failures=0,endpoint=34 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5298 | P2 | Download retry after 0 failures via 35 | failures=0,endpoint=35 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5299 | P2 | Download retry after 0 failures via 36 | failures=0,endpoint=36 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5300 | P2 | Download retry after 0 failures via 37 | failures=0,endpoint=37 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5301 | P2 | Download retry after 0 failures via 38 | failures=0,endpoint=38 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5302 | P2 | Download retry after 0 failures via 39 | failures=0,endpoint=39 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5303 | P2 | Download retry after 0 failures via 40 | failures=0,endpoint=40 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5304 | P2 | Download retry after 0 failures via 41 | failures=0,endpoint=41 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5305 | P2 | Download retry after 0 failures via 42 | failures=0,endpoint=42 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5306 | P2 | Download retry after 0 failures via 43 | failures=0,endpoint=43 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5307 | P2 | Download retry after 0 failures via 44 | failures=0,endpoint=44 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5308 | P2 | Download retry after 0 failures via 45 | failures=0,endpoint=45 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5309 | P2 | Download retry after 0 failures via 46 | failures=0,endpoint=46 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5310 | P2 | Download retry after 0 failures via 47 | failures=0,endpoint=47 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5311 | P2 | Download retry after 0 failures via 48 | failures=0,endpoint=48 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5312 | P2 | Download retry after 0 failures via 49 | failures=0,endpoint=49 | resilient | test_model_phase2_part_3.py |
| TC-MODEL-5313 | P2 | Download retry after 1 failures via 0 | failures=1,endpoint=0 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5314 | P2 | Download retry after 1 failures via 1 | failures=1,endpoint=1 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5315 | P2 | Download retry after 1 failures via 2 | failures=1,endpoint=2 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5316 | P2 | Download retry after 1 failures via 3 | failures=1,endpoint=3 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5317 | P2 | Download retry after 1 failures via 4 | failures=1,endpoint=4 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5318 | P2 | Download retry after 1 failures via 5 | failures=1,endpoint=5 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5319 | P2 | Download retry after 1 failures via 6 | failures=1,endpoint=6 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5320 | P2 | Download retry after 1 failures via 7 | failures=1,endpoint=7 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5321 | P2 | Download retry after 1 failures via 8 | failures=1,endpoint=8 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5322 | P2 | Download retry after 1 failures via 9 | failures=1,endpoint=9 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5323 | P2 | Download retry after 1 failures via 10 | failures=1,endpoint=10 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5324 | P2 | Download retry after 1 failures via 11 | failures=1,endpoint=11 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5325 | P2 | Download retry after 1 failures via 12 | failures=1,endpoint=12 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5326 | P2 | Download retry after 1 failures via 13 | failures=1,endpoint=13 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5327 | P2 | Download retry after 1 failures via 14 | failures=1,endpoint=14 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5328 | P2 | Download retry after 1 failures via 15 | failures=1,endpoint=15 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5329 | P2 | Download retry after 1 failures via 16 | failures=1,endpoint=16 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5330 | P2 | Download retry after 1 failures via 17 | failures=1,endpoint=17 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5331 | P2 | Download retry after 1 failures via 18 | failures=1,endpoint=18 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5332 | P2 | Download retry after 1 failures via 19 | failures=1,endpoint=19 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5333 | P2 | Download retry after 1 failures via 20 | failures=1,endpoint=20 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5334 | P2 | Download retry after 1 failures via 21 | failures=1,endpoint=21 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5335 | P2 | Download retry after 1 failures via 22 | failures=1,endpoint=22 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5336 | P2 | Download retry after 1 failures via 23 | failures=1,endpoint=23 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5337 | P2 | Download retry after 1 failures via 24 | failures=1,endpoint=24 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5338 | P2 | Download retry after 1 failures via 25 | failures=1,endpoint=25 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5339 | P2 | Download retry after 1 failures via 26 | failures=1,endpoint=26 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5340 | P2 | Download retry after 1 failures via 27 | failures=1,endpoint=27 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5341 | P2 | Download retry after 1 failures via 28 | failures=1,endpoint=28 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5342 | P2 | Download retry after 1 failures via 29 | failures=1,endpoint=29 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5343 | P2 | Download retry after 1 failures via 30 | failures=1,endpoint=30 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5344 | P2 | Download retry after 1 failures via 31 | failures=1,endpoint=31 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5345 | P2 | Download retry after 1 failures via 32 | failures=1,endpoint=32 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5346 | P2 | Download retry after 1 failures via 33 | failures=1,endpoint=33 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5347 | P2 | Download retry after 1 failures via 34 | failures=1,endpoint=34 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5348 | P2 | Download retry after 1 failures via 35 | failures=1,endpoint=35 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5349 | P2 | Download retry after 1 failures via 36 | failures=1,endpoint=36 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5350 | P2 | Download retry after 1 failures via 37 | failures=1,endpoint=37 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5351 | P2 | Download retry after 1 failures via 38 | failures=1,endpoint=38 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5352 | P2 | Download retry after 1 failures via 39 | failures=1,endpoint=39 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5353 | P2 | Download retry after 1 failures via 40 | failures=1,endpoint=40 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5354 | P2 | Download retry after 1 failures via 41 | failures=1,endpoint=41 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5355 | P2 | Download retry after 1 failures via 42 | failures=1,endpoint=42 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5356 | P2 | Download retry after 1 failures via 43 | failures=1,endpoint=43 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5357 | P2 | Download retry after 1 failures via 44 | failures=1,endpoint=44 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5358 | P2 | Download retry after 1 failures via 45 | failures=1,endpoint=45 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5359 | P2 | Download retry after 1 failures via 46 | failures=1,endpoint=46 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5360 | P2 | Download retry after 1 failures via 47 | failures=1,endpoint=47 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5361 | P2 | Download retry after 1 failures via 48 | failures=1,endpoint=48 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5362 | P2 | Download retry after 1 failures via 49 | failures=1,endpoint=49 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5363 | P2 | Download retry after 2 failures via 0 | failures=2,endpoint=0 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5364 | P2 | Download retry after 2 failures via 1 | failures=2,endpoint=1 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5365 | P2 | Download retry after 2 failures via 2 | failures=2,endpoint=2 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5366 | P2 | Download retry after 2 failures via 3 | failures=2,endpoint=3 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5367 | P2 | Download retry after 2 failures via 4 | failures=2,endpoint=4 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5368 | P2 | Download retry after 2 failures via 5 | failures=2,endpoint=5 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5369 | P2 | Download retry after 2 failures via 6 | failures=2,endpoint=6 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5370 | P2 | Download retry after 2 failures via 7 | failures=2,endpoint=7 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5371 | P2 | Download retry after 2 failures via 8 | failures=2,endpoint=8 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5372 | P2 | Download retry after 2 failures via 9 | failures=2,endpoint=9 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5373 | P2 | Download retry after 2 failures via 10 | failures=2,endpoint=10 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5374 | P2 | Download retry after 2 failures via 11 | failures=2,endpoint=11 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5375 | P2 | Download retry after 2 failures via 12 | failures=2,endpoint=12 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5376 | P2 | Download retry after 2 failures via 13 | failures=2,endpoint=13 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5377 | P2 | Download retry after 2 failures via 14 | failures=2,endpoint=14 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5378 | P2 | Download retry after 2 failures via 15 | failures=2,endpoint=15 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5379 | P2 | Download retry after 2 failures via 16 | failures=2,endpoint=16 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5380 | P2 | Download retry after 2 failures via 17 | failures=2,endpoint=17 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5381 | P2 | Download retry after 2 failures via 18 | failures=2,endpoint=18 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5382 | P2 | Download retry after 2 failures via 19 | failures=2,endpoint=19 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5383 | P2 | Download retry after 2 failures via 20 | failures=2,endpoint=20 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5384 | P2 | Download retry after 2 failures via 21 | failures=2,endpoint=21 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5385 | P2 | Download retry after 2 failures via 22 | failures=2,endpoint=22 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5386 | P2 | Download retry after 2 failures via 23 | failures=2,endpoint=23 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5387 | P2 | Download retry after 2 failures via 24 | failures=2,endpoint=24 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5388 | P2 | Download retry after 2 failures via 25 | failures=2,endpoint=25 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5389 | P2 | Download retry after 2 failures via 26 | failures=2,endpoint=26 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5390 | P2 | Download retry after 2 failures via 27 | failures=2,endpoint=27 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5391 | P2 | Download retry after 2 failures via 28 | failures=2,endpoint=28 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5392 | P2 | Download retry after 2 failures via 29 | failures=2,endpoint=29 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5393 | P2 | Download retry after 2 failures via 30 | failures=2,endpoint=30 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5394 | P2 | Download retry after 2 failures via 31 | failures=2,endpoint=31 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5395 | P2 | Download retry after 2 failures via 32 | failures=2,endpoint=32 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5396 | P2 | Download retry after 2 failures via 33 | failures=2,endpoint=33 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5397 | P2 | Download retry after 2 failures via 34 | failures=2,endpoint=34 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5398 | P2 | Download retry after 2 failures via 35 | failures=2,endpoint=35 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5399 | P2 | Download retry after 2 failures via 36 | failures=2,endpoint=36 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5400 | P2 | Download retry after 2 failures via 37 | failures=2,endpoint=37 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5401 | P2 | Download retry after 2 failures via 38 | failures=2,endpoint=38 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5402 | P2 | Download retry after 2 failures via 39 | failures=2,endpoint=39 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5403 | P2 | Download retry after 2 failures via 40 | failures=2,endpoint=40 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5404 | P2 | Download retry after 2 failures via 41 | failures=2,endpoint=41 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5405 | P2 | Download retry after 2 failures via 42 | failures=2,endpoint=42 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5406 | P2 | Download retry after 2 failures via 43 | failures=2,endpoint=43 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5407 | P2 | Download retry after 2 failures via 44 | failures=2,endpoint=44 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5408 | P2 | Download retry after 2 failures via 45 | failures=2,endpoint=45 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5409 | P2 | Download retry after 2 failures via 46 | failures=2,endpoint=46 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5410 | P2 | Download retry after 2 failures via 47 | failures=2,endpoint=47 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5411 | P2 | Download retry after 2 failures via 48 | failures=2,endpoint=48 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5412 | P2 | Download retry after 2 failures via 49 | failures=2,endpoint=49 | resilient | test_model_phase2_part_4.py |
| TC-MODEL-5413 | P2 | Prompt building scenario 0 | scenario=0 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5414 | P2 | Prompt building scenario 1 | scenario=1 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5415 | P2 | Prompt building scenario 2 | scenario=2 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5416 | P2 | Prompt building scenario 3 | scenario=3 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5417 | P2 | Prompt building scenario 4 | scenario=4 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5418 | P2 | Prompt building scenario 5 | scenario=5 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5419 | P2 | Prompt building scenario 6 | scenario=6 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5420 | P2 | Prompt building scenario 7 | scenario=7 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5421 | P2 | Prompt building scenario 8 | scenario=8 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5422 | P2 | Prompt building scenario 9 | scenario=9 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5423 | P2 | Prompt building scenario 10 | scenario=10 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5424 | P2 | Prompt building scenario 11 | scenario=11 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5425 | P2 | Prompt building scenario 12 | scenario=12 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5426 | P2 | Prompt building scenario 13 | scenario=13 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5427 | P2 | Prompt building scenario 14 | scenario=14 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5428 | P2 | Prompt building scenario 15 | scenario=15 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5429 | P2 | Prompt building scenario 16 | scenario=16 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5430 | P2 | Prompt building scenario 17 | scenario=17 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5431 | P2 | Prompt building scenario 18 | scenario=18 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5432 | P2 | Prompt building scenario 19 | scenario=19 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5433 | P2 | Prompt building scenario 20 | scenario=20 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5434 | P2 | Prompt building scenario 21 | scenario=21 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5435 | P2 | Prompt building scenario 22 | scenario=22 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5436 | P2 | Prompt building scenario 23 | scenario=23 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5437 | P2 | Prompt building scenario 24 | scenario=24 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5438 | P2 | Prompt building scenario 25 | scenario=25 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5439 | P2 | Prompt building scenario 26 | scenario=26 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5440 | P2 | Prompt building scenario 27 | scenario=27 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5441 | P2 | Prompt building scenario 28 | scenario=28 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5442 | P2 | Prompt building scenario 29 | scenario=29 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5443 | P2 | Prompt building scenario 30 | scenario=30 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5444 | P2 | Prompt building scenario 31 | scenario=31 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5445 | P2 | Prompt building scenario 32 | scenario=32 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5446 | P2 | Prompt building scenario 33 | scenario=33 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5447 | P2 | Prompt building scenario 34 | scenario=34 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5448 | P2 | Prompt building scenario 35 | scenario=35 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5449 | P2 | Prompt building scenario 36 | scenario=36 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5450 | P2 | Prompt building scenario 37 | scenario=37 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5451 | P2 | Prompt building scenario 38 | scenario=38 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5452 | P2 | Prompt building scenario 39 | scenario=39 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5453 | P2 | Prompt building scenario 40 | scenario=40 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5454 | P2 | Prompt building scenario 41 | scenario=41 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5455 | P2 | Prompt building scenario 42 | scenario=42 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5456 | P2 | Prompt building scenario 43 | scenario=43 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5457 | P2 | Prompt building scenario 44 | scenario=44 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5458 | P2 | Prompt building scenario 45 | scenario=45 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5459 | P2 | Prompt building scenario 46 | scenario=46 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5460 | P2 | Prompt building scenario 47 | scenario=47 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5461 | P2 | Prompt building scenario 48 | scenario=48 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5462 | P2 | Prompt building scenario 49 | scenario=49 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5463 | P2 | Prompt building scenario 50 | scenario=50 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5464 | P2 | Prompt building scenario 51 | scenario=51 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5465 | P2 | Prompt building scenario 52 | scenario=52 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5466 | P2 | Prompt building scenario 53 | scenario=53 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5467 | P2 | Prompt building scenario 54 | scenario=54 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5468 | P2 | Prompt building scenario 55 | scenario=55 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5469 | P2 | Prompt building scenario 56 | scenario=56 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5470 | P2 | Prompt building scenario 57 | scenario=57 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5471 | P2 | Prompt building scenario 58 | scenario=58 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5472 | P2 | Prompt building scenario 59 | scenario=59 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5473 | P2 | Prompt building scenario 60 | scenario=60 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5474 | P2 | Prompt building scenario 61 | scenario=61 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5475 | P2 | Prompt building scenario 62 | scenario=62 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5476 | P2 | Prompt building scenario 63 | scenario=63 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5477 | P2 | Prompt building scenario 64 | scenario=64 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5478 | P2 | Prompt building scenario 65 | scenario=65 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5479 | P2 | Prompt building scenario 66 | scenario=66 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5480 | P2 | Prompt building scenario 67 | scenario=67 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5481 | P2 | Prompt building scenario 68 | scenario=68 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5482 | P2 | Prompt building scenario 69 | scenario=69 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5483 | P2 | Prompt building scenario 70 | scenario=70 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5484 | P2 | Prompt building scenario 71 | scenario=71 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5485 | P2 | Prompt building scenario 72 | scenario=72 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5486 | P2 | Prompt building scenario 73 | scenario=73 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5487 | P2 | Prompt building scenario 74 | scenario=74 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5488 | P2 | Prompt building scenario 75 | scenario=75 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5489 | P2 | Prompt building scenario 76 | scenario=76 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5490 | P2 | Prompt building scenario 77 | scenario=77 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5491 | P2 | Prompt building scenario 78 | scenario=78 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5492 | P2 | Prompt building scenario 79 | scenario=79 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5493 | P2 | Prompt building scenario 80 | scenario=80 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5494 | P2 | Prompt building scenario 81 | scenario=81 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5495 | P2 | Prompt building scenario 82 | scenario=82 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5496 | P2 | Prompt building scenario 83 | scenario=83 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5497 | P2 | Prompt building scenario 84 | scenario=84 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5498 | P2 | Prompt building scenario 85 | scenario=85 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5499 | P2 | Prompt building scenario 86 | scenario=86 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5500 | P2 | Prompt building scenario 87 | scenario=87 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5501 | P2 | Prompt building scenario 88 | scenario=88 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5502 | P2 | Prompt building scenario 89 | scenario=89 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5503 | P2 | Prompt building scenario 90 | scenario=90 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5504 | P2 | Prompt building scenario 91 | scenario=91 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5505 | P2 | Prompt building scenario 92 | scenario=92 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5506 | P2 | Prompt building scenario 93 | scenario=93 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5507 | P2 | Prompt building scenario 94 | scenario=94 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5508 | P2 | Prompt building scenario 95 | scenario=95 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5509 | P2 | Prompt building scenario 96 | scenario=96 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5510 | P2 | Prompt building scenario 97 | scenario=97 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5511 | P2 | Prompt building scenario 98 | scenario=98 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5512 | P2 | Prompt building scenario 99 | scenario=99 | prompt built | test_model_phase2_part_5.py |
| TC-MODEL-5513 | P1 | Detect reply #0 | reply='BLOCK' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5514 | P1 | Detect reply #1 | reply='ALLOW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5515 | P1 | Detect reply #2 | reply='PASS' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5516 | P1 | Detect reply #3 | reply='REVIEW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5517 | P1 | Detect reply #4 | reply='<think>reasoning</th' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5518 | P1 | Detect reply #5 | reply='<think>x</think> ALL' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5519 | P1 | Detect reply #6 | reply='BLOCK the content' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5520 | P1 | Detect reply #7 | reply='the answer is PASS' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5521 | P1 | Detect reply #8 | reply='VERDICT: BLOCK' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5522 | P1 | Detect reply #9 | reply='moderation: ALLOW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5523 | P1 | Detect reply #10 | reply='BLOCK' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5524 | P1 | Detect reply #11 | reply='ALLOW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5525 | P1 | Detect reply #12 | reply='PASS' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5526 | P1 | Detect reply #13 | reply='REVIEW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5527 | P1 | Detect reply #14 | reply='<think>reasoning</th' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5528 | P1 | Detect reply #15 | reply='<think>x</think> ALL' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5529 | P1 | Detect reply #16 | reply='BLOCK the content' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5530 | P1 | Detect reply #17 | reply='the answer is PASS' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5531 | P1 | Detect reply #18 | reply='VERDICT: BLOCK' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5532 | P1 | Detect reply #19 | reply='moderation: ALLOW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5533 | P1 | Detect reply #20 | reply='BLOCK' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5534 | P1 | Detect reply #21 | reply='ALLOW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5535 | P1 | Detect reply #22 | reply='PASS' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5536 | P1 | Detect reply #23 | reply='REVIEW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5537 | P1 | Detect reply #24 | reply='<think>reasoning</th' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5538 | P1 | Detect reply #25 | reply='<think>x</think> ALL' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5539 | P1 | Detect reply #26 | reply='BLOCK the content' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5540 | P1 | Detect reply #27 | reply='the answer is PASS' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5541 | P1 | Detect reply #28 | reply='VERDICT: BLOCK' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5542 | P1 | Detect reply #29 | reply='moderation: ALLOW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5543 | P1 | Detect reply #30 | reply='BLOCK' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5544 | P1 | Detect reply #31 | reply='ALLOW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5545 | P1 | Detect reply #32 | reply='PASS' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5546 | P1 | Detect reply #33 | reply='REVIEW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5547 | P1 | Detect reply #34 | reply='<think>reasoning</th' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5548 | P1 | Detect reply #35 | reply='<think>x</think> ALL' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5549 | P1 | Detect reply #36 | reply='BLOCK the content' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5550 | P1 | Detect reply #37 | reply='the answer is PASS' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5551 | P1 | Detect reply #38 | reply='VERDICT: BLOCK' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5552 | P1 | Detect reply #39 | reply='moderation: ALLOW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5553 | P1 | Detect reply #40 | reply='BLOCK' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5554 | P1 | Detect reply #41 | reply='ALLOW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5555 | P1 | Detect reply #42 | reply='PASS' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5556 | P1 | Detect reply #43 | reply='REVIEW' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5557 | P1 | Detect reply #44 | reply='<think>reasoning</th' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5558 | P1 | Detect reply #45 | reply='<think>x</think> ALL' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5559 | P1 | Detect reply #46 | reply='BLOCK the content' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5560 | P1 | Detect reply #47 | reply='the answer is PASS' | matched=False | test_model_phase2_part_6.py |
| TC-MODEL-5561 | P1 | Detect reply #48 | reply='VERDICT: BLOCK' | matched=True | test_model_phase2_part_6.py |
| TC-MODEL-5562 | P1 | Detect reply #49 | reply='moderation: ALLOW' | matched=False | test_model_phase2_part_6.py |

### Phase 3 - 10,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-MODEL-0611 onward.

### Phase 4 - 100,000 cases
- Planned high-scale scenarios, IDs TC-MODEL-10611 onward.

### Phase 5 - 789,390 cases
- Planned exhaustive dimension sweep, IDs TC-MODEL-110611 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_model_phase2_part_1.py | 5013-5112 | P1 | :white_check_mark: Phase 2 |
| test_model_phase2_part_2.py | 5113-5212 | P1 | :white_check_mark: Phase 2 |
| test_model_phase2_part_3.py | 5213-5312 | P2 | :white_check_mark: Phase 2 |
| test_model_phase2_part_4.py | 5313-5412 | P2 | :white_check_mark: Phase 2 |
| test_model_phase2_part_5.py | 5413-5512 | P2 | :white_check_mark: Phase 2 |
| test_model_phase2_part_6.py | 5513-5562 | P1 | :white_check_mark: Phase 2 |

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
- Model Auto-Download
- LLM Integration
