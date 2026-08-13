# Export Module Test Documentation

## Overview
- **Total Planned:** 1,500,000
- **Phase 1:** 70 (IDs TC-EXP-001 to TC-EXP-0070) :white_check_mark: Implemented
- **Phase 2:** 600 (IDs TC-EXP-0071 to TC-EXP-0670) :white_check_mark: Implemented
- **Phase 3:** 15,000 (IDs TC-EXP-0671 to TC-EXP-15670) :hourglass: Planned
- **Phase 4:** 150,000 (IDs TC-EXP-15671 to TC-EXP-165670) :hourglass: Planned
- **Phase 5:** 1,334,330 (IDs TC-EXP-165671 to TC-EXP-1500000) :hourglass: Planned

## Dimension Matrix
| Dimension | Values (Phase 2) |
| :--- | :--- |
| Database count | 0-5 |
| Table count | 1-10 |
| Secret suffix | _KEY, _SECRET, PASSWORD, TOKEN |
| Retention days | 1-365 |
| Semantic files | present, missing |
| Log rotation | 0-10 backups |

## Test Case List

### Phase 1 - 70 cases
- 70 cases (archives, redaction, pruning).

### Phase 2 (Current) - 600 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-EXP-8124 | P1 | Archive entry users.db with 1 databases | marker=users.db,dbs=1 | included | test_export_phase2_part_1.py |
| TC-EXP-8125 | P1 | Archive entry users.db with 2 databases | marker=users.db,dbs=2 | included | test_export_phase2_part_1.py |
| TC-EXP-8126 | P1 | Archive entry users.db with 3 databases | marker=users.db,dbs=3 | included | test_export_phase2_part_1.py |
| TC-EXP-8127 | P1 | Archive entry users.db with 4 databases | marker=users.db,dbs=4 | included | test_export_phase2_part_1.py |
| TC-EXP-8128 | P1 | Archive entry users.db with 5 databases | marker=users.db,dbs=5 | included | test_export_phase2_part_1.py |
| TC-EXP-8129 | P1 | Archive entry users.db with 6 databases | marker=users.db,dbs=6 | included | test_export_phase2_part_1.py |
| TC-EXP-8130 | P1 | Archive entry users.db with 7 databases | marker=users.db,dbs=7 | included | test_export_phase2_part_1.py |
| TC-EXP-8131 | P1 | Archive entry users.db with 8 databases | marker=users.db,dbs=8 | included | test_export_phase2_part_1.py |
| TC-EXP-8132 | P1 | Archive entry users.db with 9 databases | marker=users.db,dbs=9 | included | test_export_phase2_part_1.py |
| TC-EXP-8133 | P1 | Archive entry users.db with 10 databases | marker=users.db,dbs=10 | included | test_export_phase2_part_1.py |
| TC-EXP-8134 | P1 | Archive entry users.db with 11 databases | marker=users.db,dbs=11 | included | test_export_phase2_part_1.py |
| TC-EXP-8135 | P1 | Archive entry users.db with 12 databases | marker=users.db,dbs=12 | included | test_export_phase2_part_1.py |
| TC-EXP-8136 | P1 | Archive entry users.db with 13 databases | marker=users.db,dbs=13 | included | test_export_phase2_part_1.py |
| TC-EXP-8137 | P1 | Archive entry users.db with 14 databases | marker=users.db,dbs=14 | included | test_export_phase2_part_1.py |
| TC-EXP-8138 | P1 | Archive entry users.db with 15 databases | marker=users.db,dbs=15 | included | test_export_phase2_part_1.py |
| TC-EXP-8139 | P1 | Archive entry users.db with 16 databases | marker=users.db,dbs=16 | included | test_export_phase2_part_1.py |
| TC-EXP-8140 | P1 | Archive entry users.db with 17 databases | marker=users.db,dbs=17 | included | test_export_phase2_part_1.py |
| TC-EXP-8141 | P1 | Archive entry users.db with 18 databases | marker=users.db,dbs=18 | included | test_export_phase2_part_1.py |
| TC-EXP-8142 | P1 | Archive entry users.db with 19 databases | marker=users.db,dbs=19 | included | test_export_phase2_part_1.py |
| TC-EXP-8143 | P1 | Archive entry users.db with 20 databases | marker=users.db,dbs=20 | included | test_export_phase2_part_1.py |
| TC-EXP-8144 | P1 | Archive entry users.db with 21 databases | marker=users.db,dbs=21 | included | test_export_phase2_part_1.py |
| TC-EXP-8145 | P1 | Archive entry users.db with 22 databases | marker=users.db,dbs=22 | included | test_export_phase2_part_1.py |
| TC-EXP-8146 | P1 | Archive entry moderation.log with 1 databases | marker=moderation.log,dbs=1 | included | test_export_phase2_part_1.py |
| TC-EXP-8147 | P1 | Archive entry moderation.log with 2 databases | marker=moderation.log,dbs=2 | included | test_export_phase2_part_1.py |
| TC-EXP-8148 | P1 | Archive entry moderation.log with 3 databases | marker=moderation.log,dbs=3 | included | test_export_phase2_part_1.py |
| TC-EXP-8149 | P1 | Archive entry moderation.log with 4 databases | marker=moderation.log,dbs=4 | included | test_export_phase2_part_1.py |
| TC-EXP-8150 | P1 | Archive entry moderation.log with 5 databases | marker=moderation.log,dbs=5 | included | test_export_phase2_part_1.py |
| TC-EXP-8151 | P1 | Archive entry moderation.log with 6 databases | marker=moderation.log,dbs=6 | included | test_export_phase2_part_1.py |
| TC-EXP-8152 | P1 | Archive entry moderation.log with 7 databases | marker=moderation.log,dbs=7 | included | test_export_phase2_part_1.py |
| TC-EXP-8153 | P1 | Archive entry moderation.log with 8 databases | marker=moderation.log,dbs=8 | included | test_export_phase2_part_1.py |
| TC-EXP-8154 | P1 | Archive entry moderation.log with 9 databases | marker=moderation.log,dbs=9 | included | test_export_phase2_part_1.py |
| TC-EXP-8155 | P1 | Archive entry moderation.log with 10 databases | marker=moderation.log,dbs=10 | included | test_export_phase2_part_1.py |
| TC-EXP-8156 | P1 | Archive entry moderation.log with 11 databases | marker=moderation.log,dbs=11 | included | test_export_phase2_part_1.py |
| TC-EXP-8157 | P1 | Archive entry moderation.log with 12 databases | marker=moderation.log,dbs=12 | included | test_export_phase2_part_1.py |
| TC-EXP-8158 | P1 | Archive entry moderation.log with 13 databases | marker=moderation.log,dbs=13 | included | test_export_phase2_part_1.py |
| TC-EXP-8159 | P1 | Archive entry moderation.log with 14 databases | marker=moderation.log,dbs=14 | included | test_export_phase2_part_1.py |
| TC-EXP-8160 | P1 | Archive entry moderation.log with 15 databases | marker=moderation.log,dbs=15 | included | test_export_phase2_part_1.py |
| TC-EXP-8161 | P1 | Archive entry moderation.log with 16 databases | marker=moderation.log,dbs=16 | included | test_export_phase2_part_1.py |
| TC-EXP-8162 | P1 | Archive entry moderation.log with 17 databases | marker=moderation.log,dbs=17 | included | test_export_phase2_part_1.py |
| TC-EXP-8163 | P1 | Archive entry moderation.log with 18 databases | marker=moderation.log,dbs=18 | included | test_export_phase2_part_1.py |
| TC-EXP-8164 | P1 | Archive entry moderation.log with 19 databases | marker=moderation.log,dbs=19 | included | test_export_phase2_part_1.py |
| TC-EXP-8165 | P1 | Archive entry moderation.log with 20 databases | marker=moderation.log,dbs=20 | included | test_export_phase2_part_1.py |
| TC-EXP-8166 | P1 | Archive entry moderation.log with 21 databases | marker=moderation.log,dbs=21 | included | test_export_phase2_part_1.py |
| TC-EXP-8167 | P1 | Archive entry moderation.log with 22 databases | marker=moderation.log,dbs=22 | included | test_export_phase2_part_1.py |
| TC-EXP-8168 | P1 | Archive entry political.index with 1 databases | marker=political.index,dbs=1 | included | test_export_phase2_part_1.py |
| TC-EXP-8169 | P1 | Archive entry political.index with 2 databases | marker=political.index,dbs=2 | included | test_export_phase2_part_1.py |
| TC-EXP-8170 | P1 | Archive entry political.index with 3 databases | marker=political.index,dbs=3 | included | test_export_phase2_part_1.py |
| TC-EXP-8171 | P1 | Archive entry political.index with 4 databases | marker=political.index,dbs=4 | included | test_export_phase2_part_1.py |
| TC-EXP-8172 | P1 | Archive entry political.index with 5 databases | marker=political.index,dbs=5 | included | test_export_phase2_part_1.py |
| TC-EXP-8173 | P1 | Archive entry political.index with 6 databases | marker=political.index,dbs=6 | included | test_export_phase2_part_1.py |
| TC-EXP-8174 | P1 | Archive entry political.index with 7 databases | marker=political.index,dbs=7 | included | test_export_phase2_part_1.py |
| TC-EXP-8175 | P1 | Archive entry political.index with 8 databases | marker=political.index,dbs=8 | included | test_export_phase2_part_1.py |
| TC-EXP-8176 | P1 | Archive entry political.index with 9 databases | marker=political.index,dbs=9 | included | test_export_phase2_part_1.py |
| TC-EXP-8177 | P1 | Archive entry political.index with 10 databases | marker=political.index,dbs=10 | included | test_export_phase2_part_1.py |
| TC-EXP-8178 | P1 | Archive entry political.index with 11 databases | marker=political.index,dbs=11 | included | test_export_phase2_part_1.py |
| TC-EXP-8179 | P1 | Archive entry political.index with 12 databases | marker=political.index,dbs=12 | included | test_export_phase2_part_1.py |
| TC-EXP-8180 | P1 | Archive entry political.index with 13 databases | marker=political.index,dbs=13 | included | test_export_phase2_part_1.py |
| TC-EXP-8181 | P1 | Archive entry political.index with 14 databases | marker=political.index,dbs=14 | included | test_export_phase2_part_1.py |
| TC-EXP-8182 | P1 | Archive entry political.index with 15 databases | marker=political.index,dbs=15 | included | test_export_phase2_part_1.py |
| TC-EXP-8183 | P1 | Archive entry political.index with 16 databases | marker=political.index,dbs=16 | included | test_export_phase2_part_1.py |
| TC-EXP-8184 | P1 | Archive entry political.index with 17 databases | marker=political.index,dbs=17 | included | test_export_phase2_part_1.py |
| TC-EXP-8185 | P1 | Archive entry political.index with 18 databases | marker=political.index,dbs=18 | included | test_export_phase2_part_1.py |
| TC-EXP-8186 | P1 | Archive entry political.index with 19 databases | marker=political.index,dbs=19 | included | test_export_phase2_part_1.py |
| TC-EXP-8187 | P1 | Archive entry political.index with 20 databases | marker=political.index,dbs=20 | included | test_export_phase2_part_1.py |
| TC-EXP-8188 | P1 | Archive entry political.index with 21 databases | marker=political.index,dbs=21 | included | test_export_phase2_part_1.py |
| TC-EXP-8189 | P1 | Archive entry political.index with 22 databases | marker=political.index,dbs=22 | included | test_export_phase2_part_1.py |
| TC-EXP-8190 | P1 | Archive entry political.json with 1 databases | marker=political.json,dbs=1 | included | test_export_phase2_part_1.py |
| TC-EXP-8191 | P1 | Archive entry political.json with 2 databases | marker=political.json,dbs=2 | included | test_export_phase2_part_1.py |
| TC-EXP-8192 | P1 | Archive entry political.json with 3 databases | marker=political.json,dbs=3 | included | test_export_phase2_part_1.py |
| TC-EXP-8193 | P1 | Archive entry political.json with 4 databases | marker=political.json,dbs=4 | included | test_export_phase2_part_1.py |
| TC-EXP-8194 | P1 | Archive entry political.json with 5 databases | marker=political.json,dbs=5 | included | test_export_phase2_part_1.py |
| TC-EXP-8195 | P1 | Archive entry political.json with 6 databases | marker=political.json,dbs=6 | included | test_export_phase2_part_1.py |
| TC-EXP-8196 | P1 | Archive entry political.json with 7 databases | marker=political.json,dbs=7 | included | test_export_phase2_part_1.py |
| TC-EXP-8197 | P1 | Archive entry political.json with 8 databases | marker=political.json,dbs=8 | included | test_export_phase2_part_1.py |
| TC-EXP-8198 | P1 | Archive entry political.json with 9 databases | marker=political.json,dbs=9 | included | test_export_phase2_part_1.py |
| TC-EXP-8199 | P1 | Archive entry political.json with 10 databases | marker=political.json,dbs=10 | included | test_export_phase2_part_1.py |
| TC-EXP-8200 | P1 | Archive entry political.json with 11 databases | marker=political.json,dbs=11 | included | test_export_phase2_part_1.py |
| TC-EXP-8201 | P1 | Archive entry political.json with 12 databases | marker=political.json,dbs=12 | included | test_export_phase2_part_1.py |
| TC-EXP-8202 | P1 | Archive entry political.json with 13 databases | marker=political.json,dbs=13 | included | test_export_phase2_part_1.py |
| TC-EXP-8203 | P1 | Archive entry political.json with 14 databases | marker=political.json,dbs=14 | included | test_export_phase2_part_1.py |
| TC-EXP-8204 | P1 | Archive entry political.json with 15 databases | marker=political.json,dbs=15 | included | test_export_phase2_part_1.py |
| TC-EXP-8205 | P1 | Archive entry political.json with 16 databases | marker=political.json,dbs=16 | included | test_export_phase2_part_1.py |
| TC-EXP-8206 | P1 | Archive entry political.json with 17 databases | marker=political.json,dbs=17 | included | test_export_phase2_part_1.py |
| TC-EXP-8207 | P1 | Archive entry political.json with 18 databases | marker=political.json,dbs=18 | included | test_export_phase2_part_1.py |
| TC-EXP-8208 | P1 | Archive entry political.json with 19 databases | marker=political.json,dbs=19 | included | test_export_phase2_part_1.py |
| TC-EXP-8209 | P1 | Archive entry political.json with 20 databases | marker=political.json,dbs=20 | included | test_export_phase2_part_1.py |
| TC-EXP-8210 | P1 | Archive entry political.json with 21 databases | marker=political.json,dbs=21 | included | test_export_phase2_part_1.py |
| TC-EXP-8211 | P1 | Archive entry political.json with 22 databases | marker=political.json,dbs=22 | included | test_export_phase2_part_1.py |
| TC-EXP-8212 | P1 | Archive entry config/.env with 1 databases | marker=config/.env,dbs=1 | included | test_export_phase2_part_1.py |
| TC-EXP-8213 | P1 | Archive entry config/.env with 2 databases | marker=config/.env,dbs=2 | included | test_export_phase2_part_1.py |
| TC-EXP-8214 | P1 | Archive entry config/.env with 3 databases | marker=config/.env,dbs=3 | included | test_export_phase2_part_1.py |
| TC-EXP-8215 | P1 | Archive entry config/.env with 4 databases | marker=config/.env,dbs=4 | included | test_export_phase2_part_1.py |
| TC-EXP-8216 | P1 | Archive entry config/.env with 5 databases | marker=config/.env,dbs=5 | included | test_export_phase2_part_1.py |
| TC-EXP-8217 | P1 | Archive entry config/.env with 6 databases | marker=config/.env,dbs=6 | included | test_export_phase2_part_1.py |
| TC-EXP-8218 | P1 | Archive entry config/.env with 7 databases | marker=config/.env,dbs=7 | included | test_export_phase2_part_1.py |
| TC-EXP-8219 | P1 | Archive entry config/.env with 8 databases | marker=config/.env,dbs=8 | included | test_export_phase2_part_1.py |
| TC-EXP-8220 | P1 | Archive entry config/.env with 9 databases | marker=config/.env,dbs=9 | included | test_export_phase2_part_1.py |
| TC-EXP-8221 | P1 | Archive entry config/.env with 10 databases | marker=config/.env,dbs=10 | included | test_export_phase2_part_1.py |
| TC-EXP-8222 | P1 | Archive entry config/.env with 11 databases | marker=config/.env,dbs=11 | included | test_export_phase2_part_1.py |
| TC-EXP-8223 | P1 | Archive entry config/.env with 12 databases | marker=config/.env,dbs=12 | included | test_export_phase2_part_1.py |
| TC-EXP-8224 | P1 | Archive entry config/.env with 13 databases | marker=config/.env,dbs=13 | included | test_export_phase2_part_2.py |
| TC-EXP-8225 | P1 | Archive entry config/.env with 14 databases | marker=config/.env,dbs=14 | included | test_export_phase2_part_2.py |
| TC-EXP-8226 | P1 | Archive entry config/.env with 15 databases | marker=config/.env,dbs=15 | included | test_export_phase2_part_2.py |
| TC-EXP-8227 | P1 | Archive entry config/.env with 16 databases | marker=config/.env,dbs=16 | included | test_export_phase2_part_2.py |
| TC-EXP-8228 | P1 | Archive entry config/.env with 17 databases | marker=config/.env,dbs=17 | included | test_export_phase2_part_2.py |
| TC-EXP-8229 | P1 | Archive entry config/.env with 18 databases | marker=config/.env,dbs=18 | included | test_export_phase2_part_2.py |
| TC-EXP-8230 | P1 | Archive entry config/.env with 19 databases | marker=config/.env,dbs=19 | included | test_export_phase2_part_2.py |
| TC-EXP-8231 | P1 | Archive entry config/.env with 20 databases | marker=config/.env,dbs=20 | included | test_export_phase2_part_2.py |
| TC-EXP-8232 | P1 | Archive entry config/.env with 21 databases | marker=config/.env,dbs=21 | included | test_export_phase2_part_2.py |
| TC-EXP-8233 | P1 | Archive entry config/.env with 22 databases | marker=config/.env,dbs=22 | included | test_export_phase2_part_2.py |
| TC-EXP-8234 | P1 | Archive entry export_metadata.json with 1 databases | marker=export_metadata.json,dbs=1 | included | test_export_phase2_part_2.py |
| TC-EXP-8235 | P1 | Archive entry export_metadata.json with 2 databases | marker=export_metadata.json,dbs=2 | included | test_export_phase2_part_2.py |
| TC-EXP-8236 | P1 | Archive entry export_metadata.json with 3 databases | marker=export_metadata.json,dbs=3 | included | test_export_phase2_part_2.py |
| TC-EXP-8237 | P1 | Archive entry export_metadata.json with 4 databases | marker=export_metadata.json,dbs=4 | included | test_export_phase2_part_2.py |
| TC-EXP-8238 | P1 | Archive entry export_metadata.json with 5 databases | marker=export_metadata.json,dbs=5 | included | test_export_phase2_part_2.py |
| TC-EXP-8239 | P1 | Archive entry export_metadata.json with 6 databases | marker=export_metadata.json,dbs=6 | included | test_export_phase2_part_2.py |
| TC-EXP-8240 | P1 | Archive entry export_metadata.json with 7 databases | marker=export_metadata.json,dbs=7 | included | test_export_phase2_part_2.py |
| TC-EXP-8241 | P1 | Archive entry export_metadata.json with 8 databases | marker=export_metadata.json,dbs=8 | included | test_export_phase2_part_2.py |
| TC-EXP-8242 | P1 | Archive entry export_metadata.json with 9 databases | marker=export_metadata.json,dbs=9 | included | test_export_phase2_part_2.py |
| TC-EXP-8243 | P1 | Archive entry export_metadata.json with 10 databases | marker=export_metadata.json,dbs=10 | included | test_export_phase2_part_2.py |
| TC-EXP-8244 | P1 | Archive entry export_metadata.json with 11 databases | marker=export_metadata.json,dbs=11 | included | test_export_phase2_part_2.py |
| TC-EXP-8245 | P1 | Archive entry export_metadata.json with 12 databases | marker=export_metadata.json,dbs=12 | included | test_export_phase2_part_2.py |
| TC-EXP-8246 | P1 | Archive entry export_metadata.json with 13 databases | marker=export_metadata.json,dbs=13 | included | test_export_phase2_part_2.py |
| TC-EXP-8247 | P1 | Archive entry export_metadata.json with 14 databases | marker=export_metadata.json,dbs=14 | included | test_export_phase2_part_2.py |
| TC-EXP-8248 | P1 | Archive entry export_metadata.json with 15 databases | marker=export_metadata.json,dbs=15 | included | test_export_phase2_part_2.py |
| TC-EXP-8249 | P1 | Archive entry export_metadata.json with 16 databases | marker=export_metadata.json,dbs=16 | included | test_export_phase2_part_2.py |
| TC-EXP-8250 | P1 | Archive entry export_metadata.json with 17 databases | marker=export_metadata.json,dbs=17 | included | test_export_phase2_part_2.py |
| TC-EXP-8251 | P1 | Archive entry export_metadata.json with 18 databases | marker=export_metadata.json,dbs=18 | included | test_export_phase2_part_2.py |
| TC-EXP-8252 | P1 | Archive entry export_metadata.json with 19 databases | marker=export_metadata.json,dbs=19 | included | test_export_phase2_part_2.py |
| TC-EXP-8253 | P1 | Archive entry export_metadata.json with 20 databases | marker=export_metadata.json,dbs=20 | included | test_export_phase2_part_2.py |
| TC-EXP-8254 | P1 | Archive entry export_metadata.json with 21 databases | marker=export_metadata.json,dbs=21 | included | test_export_phase2_part_2.py |
| TC-EXP-8255 | P1 | Archive entry export_metadata.json with 22 databases | marker=export_metadata.json,dbs=22 | included | test_export_phase2_part_2.py |
| TC-EXP-8256 | P1 | Archive entry settings_snapshot.json with 1 databases | marker=settings_snapshot.json,dbs=1 | included | test_export_phase2_part_2.py |
| TC-EXP-8257 | P1 | Archive entry settings_snapshot.json with 2 databases | marker=settings_snapshot.json,dbs=2 | included | test_export_phase2_part_2.py |
| TC-EXP-8258 | P1 | Archive entry settings_snapshot.json with 3 databases | marker=settings_snapshot.json,dbs=3 | included | test_export_phase2_part_2.py |
| TC-EXP-8259 | P1 | Archive entry settings_snapshot.json with 4 databases | marker=settings_snapshot.json,dbs=4 | included | test_export_phase2_part_2.py |
| TC-EXP-8260 | P1 | Archive entry settings_snapshot.json with 5 databases | marker=settings_snapshot.json,dbs=5 | included | test_export_phase2_part_2.py |
| TC-EXP-8261 | P1 | Archive entry settings_snapshot.json with 6 databases | marker=settings_snapshot.json,dbs=6 | included | test_export_phase2_part_2.py |
| TC-EXP-8262 | P1 | Archive entry settings_snapshot.json with 7 databases | marker=settings_snapshot.json,dbs=7 | included | test_export_phase2_part_2.py |
| TC-EXP-8263 | P1 | Archive entry settings_snapshot.json with 8 databases | marker=settings_snapshot.json,dbs=8 | included | test_export_phase2_part_2.py |
| TC-EXP-8264 | P1 | Archive entry settings_snapshot.json with 9 databases | marker=settings_snapshot.json,dbs=9 | included | test_export_phase2_part_2.py |
| TC-EXP-8265 | P1 | Archive entry settings_snapshot.json with 10 databases | marker=settings_snapshot.json,dbs=10 | included | test_export_phase2_part_2.py |
| TC-EXP-8266 | P1 | Archive entry settings_snapshot.json with 11 databases | marker=settings_snapshot.json,dbs=11 | included | test_export_phase2_part_2.py |
| TC-EXP-8267 | P1 | Archive entry settings_snapshot.json with 12 databases | marker=settings_snapshot.json,dbs=12 | included | test_export_phase2_part_2.py |
| TC-EXP-8268 | P1 | Archive entry settings_snapshot.json with 13 databases | marker=settings_snapshot.json,dbs=13 | included | test_export_phase2_part_2.py |
| TC-EXP-8269 | P1 | Archive entry settings_snapshot.json with 14 databases | marker=settings_snapshot.json,dbs=14 | included | test_export_phase2_part_2.py |
| TC-EXP-8270 | P1 | Archive entry settings_snapshot.json with 15 databases | marker=settings_snapshot.json,dbs=15 | included | test_export_phase2_part_2.py |
| TC-EXP-8271 | P1 | Archive entry settings_snapshot.json with 16 databases | marker=settings_snapshot.json,dbs=16 | included | test_export_phase2_part_2.py |
| TC-EXP-8272 | P1 | Archive entry settings_snapshot.json with 17 databases | marker=settings_snapshot.json,dbs=17 | included | test_export_phase2_part_2.py |
| TC-EXP-8273 | P1 | Archive entry settings_snapshot.json with 18 databases | marker=settings_snapshot.json,dbs=18 | included | test_export_phase2_part_2.py |
| TC-EXP-8278 | P2 | Redaction SOME_API_KEY #0 | suffix=SOME_API_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8279 | P2 | Redaction SOME_API_KEY #1 | suffix=SOME_API_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8280 | P2 | Redaction SOME_API_KEY #2 | suffix=SOME_API_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8281 | P2 | Redaction SOME_API_KEY #3 | suffix=SOME_API_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8282 | P2 | Redaction SOME_API_KEY #4 | suffix=SOME_API_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8283 | P2 | Redaction SOME_SECRET #0 | suffix=SOME_SECRET | redacted | test_export_phase2_part_2.py |
| TC-EXP-8284 | P2 | Redaction SOME_SECRET #1 | suffix=SOME_SECRET | redacted | test_export_phase2_part_2.py |
| TC-EXP-8285 | P2 | Redaction SOME_SECRET #2 | suffix=SOME_SECRET | redacted | test_export_phase2_part_2.py |
| TC-EXP-8286 | P2 | Redaction SOME_SECRET #3 | suffix=SOME_SECRET | redacted | test_export_phase2_part_2.py |
| TC-EXP-8287 | P2 | Redaction SOME_SECRET #4 | suffix=SOME_SECRET | redacted | test_export_phase2_part_2.py |
| TC-EXP-8288 | P2 | Redaction SOME_PASSWORD #0 | suffix=SOME_PASSWORD | redacted | test_export_phase2_part_2.py |
| TC-EXP-8289 | P2 | Redaction SOME_PASSWORD #1 | suffix=SOME_PASSWORD | redacted | test_export_phase2_part_2.py |
| TC-EXP-8290 | P2 | Redaction SOME_PASSWORD #2 | suffix=SOME_PASSWORD | redacted | test_export_phase2_part_2.py |
| TC-EXP-8291 | P2 | Redaction SOME_PASSWORD #3 | suffix=SOME_PASSWORD | redacted | test_export_phase2_part_2.py |
| TC-EXP-8292 | P2 | Redaction SOME_PASSWORD #4 | suffix=SOME_PASSWORD | redacted | test_export_phase2_part_2.py |
| TC-EXP-8293 | P2 | Redaction SOME_TOKEN #0 | suffix=SOME_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8294 | P2 | Redaction SOME_TOKEN #1 | suffix=SOME_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8295 | P2 | Redaction SOME_TOKEN #2 | suffix=SOME_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8296 | P2 | Redaction SOME_TOKEN #3 | suffix=SOME_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8297 | P2 | Redaction SOME_TOKEN #4 | suffix=SOME_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8298 | P2 | Redaction SECRET_VALUE #0 | suffix=SECRET_VALUE | redacted | test_export_phase2_part_2.py |
| TC-EXP-8299 | P2 | Redaction SECRET_VALUE #1 | suffix=SECRET_VALUE | redacted | test_export_phase2_part_2.py |
| TC-EXP-8300 | P2 | Redaction SECRET_VALUE #2 | suffix=SECRET_VALUE | redacted | test_export_phase2_part_2.py |
| TC-EXP-8301 | P2 | Redaction SECRET_VALUE #3 | suffix=SECRET_VALUE | redacted | test_export_phase2_part_2.py |
| TC-EXP-8302 | P2 | Redaction SECRET_VALUE #4 | suffix=SECRET_VALUE | redacted | test_export_phase2_part_2.py |
| TC-EXP-8303 | P2 | Redaction API_TOKEN #0 | suffix=API_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8304 | P2 | Redaction API_TOKEN #1 | suffix=API_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8305 | P2 | Redaction API_TOKEN #2 | suffix=API_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8306 | P2 | Redaction API_TOKEN #3 | suffix=API_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8307 | P2 | Redaction API_TOKEN #4 | suffix=API_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8308 | P2 | Redaction DB_PASSWORD #0 | suffix=DB_PASSWORD | redacted | test_export_phase2_part_2.py |
| TC-EXP-8309 | P2 | Redaction DB_PASSWORD #1 | suffix=DB_PASSWORD | redacted | test_export_phase2_part_2.py |
| TC-EXP-8310 | P2 | Redaction DB_PASSWORD #2 | suffix=DB_PASSWORD | redacted | test_export_phase2_part_2.py |
| TC-EXP-8311 | P2 | Redaction DB_PASSWORD #3 | suffix=DB_PASSWORD | redacted | test_export_phase2_part_2.py |
| TC-EXP-8312 | P2 | Redaction DB_PASSWORD #4 | suffix=DB_PASSWORD | redacted | test_export_phase2_part_2.py |
| TC-EXP-8313 | P2 | Redaction ACCESS_KEY #0 | suffix=ACCESS_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8314 | P2 | Redaction ACCESS_KEY #1 | suffix=ACCESS_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8315 | P2 | Redaction ACCESS_KEY #2 | suffix=ACCESS_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8316 | P2 | Redaction ACCESS_KEY #3 | suffix=ACCESS_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8317 | P2 | Redaction ACCESS_KEY #4 | suffix=ACCESS_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8318 | P2 | Redaction AUTH_TOKEN #0 | suffix=AUTH_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8319 | P2 | Redaction AUTH_TOKEN #1 | suffix=AUTH_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8320 | P2 | Redaction AUTH_TOKEN #2 | suffix=AUTH_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8321 | P2 | Redaction AUTH_TOKEN #3 | suffix=AUTH_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8322 | P2 | Redaction AUTH_TOKEN #4 | suffix=AUTH_TOKEN | redacted | test_export_phase2_part_2.py |
| TC-EXP-8323 | P2 | Redaction PRIVATE_KEY #0 | suffix=PRIVATE_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8324 | P2 | Redaction PRIVATE_KEY #1 | suffix=PRIVATE_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8325 | P2 | Redaction PRIVATE_KEY #2 | suffix=PRIVATE_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8326 | P2 | Redaction PRIVATE_KEY #3 | suffix=PRIVATE_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8327 | P2 | Redaction PRIVATE_KEY #4 | suffix=PRIVATE_KEY | redacted | test_export_phase2_part_2.py |
| TC-EXP-8328 | P2 | Redaction APP_SECRET #0 | suffix=APP_SECRET | redacted | test_export_phase2_part_3.py |
| TC-EXP-8329 | P2 | Redaction APP_SECRET #1 | suffix=APP_SECRET | redacted | test_export_phase2_part_3.py |
| TC-EXP-8330 | P2 | Redaction APP_SECRET #2 | suffix=APP_SECRET | redacted | test_export_phase2_part_3.py |
| TC-EXP-8331 | P2 | Redaction APP_SECRET #3 | suffix=APP_SECRET | redacted | test_export_phase2_part_3.py |
| TC-EXP-8332 | P2 | Redaction APP_SECRET #4 | suffix=APP_SECRET | redacted | test_export_phase2_part_3.py |
| TC-EXP-8333 | P2 | Redaction LOGIN_PASSWORD #0 | suffix=LOGIN_PASSWORD | redacted | test_export_phase2_part_3.py |
| TC-EXP-8334 | P2 | Redaction LOGIN_PASSWORD #1 | suffix=LOGIN_PASSWORD | redacted | test_export_phase2_part_3.py |
| TC-EXP-8335 | P2 | Redaction LOGIN_PASSWORD #2 | suffix=LOGIN_PASSWORD | redacted | test_export_phase2_part_3.py |
| TC-EXP-8336 | P2 | Redaction LOGIN_PASSWORD #3 | suffix=LOGIN_PASSWORD | redacted | test_export_phase2_part_3.py |
| TC-EXP-8337 | P2 | Redaction LOGIN_PASSWORD #4 | suffix=LOGIN_PASSWORD | redacted | test_export_phase2_part_3.py |
| TC-EXP-8338 | P2 | Redaction SESSION_TOKEN #0 | suffix=SESSION_TOKEN | redacted | test_export_phase2_part_3.py |
| TC-EXP-8339 | P2 | Redaction SESSION_TOKEN #1 | suffix=SESSION_TOKEN | redacted | test_export_phase2_part_3.py |
| TC-EXP-8340 | P2 | Redaction SESSION_TOKEN #2 | suffix=SESSION_TOKEN | redacted | test_export_phase2_part_3.py |
| TC-EXP-8341 | P2 | Redaction SESSION_TOKEN #3 | suffix=SESSION_TOKEN | redacted | test_export_phase2_part_3.py |
| TC-EXP-8342 | P2 | Redaction SESSION_TOKEN #4 | suffix=SESSION_TOKEN | redacted | test_export_phase2_part_3.py |
| TC-EXP-8343 | P2 | Redaction WALLET_KEY #0 | suffix=WALLET_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8344 | P2 | Redaction WALLET_KEY #1 | suffix=WALLET_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8345 | P2 | Redaction WALLET_KEY #2 | suffix=WALLET_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8346 | P2 | Redaction WALLET_KEY #3 | suffix=WALLET_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8347 | P2 | Redaction WALLET_KEY #4 | suffix=WALLET_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8348 | P2 | Redaction PASS_KEY #0 | suffix=PASS_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8349 | P2 | Redaction PASS_KEY #1 | suffix=PASS_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8350 | P2 | Redaction PASS_KEY #2 | suffix=PASS_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8351 | P2 | Redaction PASS_KEY #3 | suffix=PASS_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8352 | P2 | Redaction PASS_KEY #4 | suffix=PASS_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8353 | P2 | Redaction SECRET_SALT #0 | suffix=SECRET_SALT | redacted | test_export_phase2_part_3.py |
| TC-EXP-8354 | P2 | Redaction SECRET_SALT #1 | suffix=SECRET_SALT | redacted | test_export_phase2_part_3.py |
| TC-EXP-8355 | P2 | Redaction SECRET_SALT #2 | suffix=SECRET_SALT | redacted | test_export_phase2_part_3.py |
| TC-EXP-8356 | P2 | Redaction SECRET_SALT #3 | suffix=SECRET_SALT | redacted | test_export_phase2_part_3.py |
| TC-EXP-8357 | P2 | Redaction SECRET_SALT #4 | suffix=SECRET_SALT | redacted | test_export_phase2_part_3.py |
| TC-EXP-8358 | P2 | Redaction TOKEN_SECRET #0 | suffix=TOKEN_SECRET | redacted | test_export_phase2_part_3.py |
| TC-EXP-8359 | P2 | Redaction TOKEN_SECRET #1 | suffix=TOKEN_SECRET | redacted | test_export_phase2_part_3.py |
| TC-EXP-8360 | P2 | Redaction TOKEN_SECRET #2 | suffix=TOKEN_SECRET | redacted | test_export_phase2_part_3.py |
| TC-EXP-8361 | P2 | Redaction TOKEN_SECRET #3 | suffix=TOKEN_SECRET | redacted | test_export_phase2_part_3.py |
| TC-EXP-8362 | P2 | Redaction TOKEN_SECRET #4 | suffix=TOKEN_SECRET | redacted | test_export_phase2_part_3.py |
| TC-EXP-8363 | P2 | Redaction PASSWORD_1 #0 | suffix=PASSWORD_1 | redacted | test_export_phase2_part_3.py |
| TC-EXP-8364 | P2 | Redaction PASSWORD_1 #1 | suffix=PASSWORD_1 | redacted | test_export_phase2_part_3.py |
| TC-EXP-8365 | P2 | Redaction PASSWORD_1 #2 | suffix=PASSWORD_1 | redacted | test_export_phase2_part_3.py |
| TC-EXP-8366 | P2 | Redaction PASSWORD_1 #3 | suffix=PASSWORD_1 | redacted | test_export_phase2_part_3.py |
| TC-EXP-8367 | P2 | Redaction PASSWORD_1 #4 | suffix=PASSWORD_1 | redacted | test_export_phase2_part_3.py |
| TC-EXP-8368 | P2 | Redaction KEY_PAIR #0 | suffix=KEY_PAIR | redacted | test_export_phase2_part_3.py |
| TC-EXP-8369 | P2 | Redaction KEY_PAIR #1 | suffix=KEY_PAIR | redacted | test_export_phase2_part_3.py |
| TC-EXP-8370 | P2 | Redaction KEY_PAIR #2 | suffix=KEY_PAIR | redacted | test_export_phase2_part_3.py |
| TC-EXP-8371 | P2 | Redaction KEY_PAIR #3 | suffix=KEY_PAIR | redacted | test_export_phase2_part_3.py |
| TC-EXP-8372 | P2 | Redaction KEY_PAIR #4 | suffix=KEY_PAIR | redacted | test_export_phase2_part_3.py |
| TC-EXP-8373 | P2 | Redaction MASTER_KEY #0 | suffix=MASTER_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8374 | P2 | Redaction MASTER_KEY #1 | suffix=MASTER_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8375 | P2 | Redaction MASTER_KEY #2 | suffix=MASTER_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8376 | P2 | Redaction MASTER_KEY #3 | suffix=MASTER_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8377 | P2 | Redaction MASTER_KEY #4 | suffix=MASTER_KEY | redacted | test_export_phase2_part_3.py |
| TC-EXP-8378 | P1 | Manifest field project with metadata 0 | field=project,metadata=0 | present | test_export_phase2_part_3.py |
| TC-EXP-8379 | P1 | Manifest field project with metadata 1 | field=project,metadata=1 | present | test_export_phase2_part_3.py |
| TC-EXP-8380 | P1 | Manifest field project with metadata 2 | field=project,metadata=2 | present | test_export_phase2_part_3.py |
| TC-EXP-8381 | P1 | Manifest field project with metadata 3 | field=project,metadata=3 | present | test_export_phase2_part_3.py |
| TC-EXP-8382 | P1 | Manifest field project with metadata 4 | field=project,metadata=4 | present | test_export_phase2_part_3.py |
| TC-EXP-8383 | P1 | Manifest field project with metadata 5 | field=project,metadata=5 | present | test_export_phase2_part_3.py |
| TC-EXP-8384 | P1 | Manifest field project with metadata 6 | field=project,metadata=6 | present | test_export_phase2_part_3.py |
| TC-EXP-8385 | P1 | Manifest field project with metadata 7 | field=project,metadata=7 | present | test_export_phase2_part_3.py |
| TC-EXP-8386 | P1 | Manifest field project with metadata 8 | field=project,metadata=8 | present | test_export_phase2_part_3.py |
| TC-EXP-8387 | P1 | Manifest field project with metadata 9 | field=project,metadata=9 | present | test_export_phase2_part_3.py |
| TC-EXP-8388 | P1 | Manifest field project with metadata 10 | field=project,metadata=10 | present | test_export_phase2_part_3.py |
| TC-EXP-8389 | P1 | Manifest field project with metadata 11 | field=project,metadata=11 | present | test_export_phase2_part_3.py |
| TC-EXP-8390 | P1 | Manifest field project with metadata 12 | field=project,metadata=12 | present | test_export_phase2_part_3.py |
| TC-EXP-8391 | P1 | Manifest field exported_at with metadata 0 | field=exported_at,metadata=0 | present | test_export_phase2_part_3.py |
| TC-EXP-8392 | P1 | Manifest field exported_at with metadata 1 | field=exported_at,metadata=1 | present | test_export_phase2_part_3.py |
| TC-EXP-8393 | P1 | Manifest field exported_at with metadata 2 | field=exported_at,metadata=2 | present | test_export_phase2_part_3.py |
| TC-EXP-8394 | P1 | Manifest field exported_at with metadata 3 | field=exported_at,metadata=3 | present | test_export_phase2_part_3.py |
| TC-EXP-8395 | P1 | Manifest field exported_at with metadata 4 | field=exported_at,metadata=4 | present | test_export_phase2_part_3.py |
| TC-EXP-8396 | P1 | Manifest field exported_at with metadata 5 | field=exported_at,metadata=5 | present | test_export_phase2_part_3.py |
| TC-EXP-8397 | P1 | Manifest field exported_at with metadata 6 | field=exported_at,metadata=6 | present | test_export_phase2_part_3.py |
| TC-EXP-8398 | P1 | Manifest field exported_at with metadata 7 | field=exported_at,metadata=7 | present | test_export_phase2_part_3.py |
| TC-EXP-8399 | P1 | Manifest field exported_at with metadata 8 | field=exported_at,metadata=8 | present | test_export_phase2_part_3.py |
| TC-EXP-8400 | P1 | Manifest field exported_at with metadata 9 | field=exported_at,metadata=9 | present | test_export_phase2_part_3.py |
| TC-EXP-8401 | P1 | Manifest field exported_at with metadata 10 | field=exported_at,metadata=10 | present | test_export_phase2_part_3.py |
| TC-EXP-8402 | P1 | Manifest field exported_at with metadata 11 | field=exported_at,metadata=11 | present | test_export_phase2_part_3.py |
| TC-EXP-8403 | P1 | Manifest field exported_at with metadata 12 | field=exported_at,metadata=12 | present | test_export_phase2_part_3.py |
| TC-EXP-8404 | P1 | Manifest field databases with metadata 0 | field=databases,metadata=0 | present | test_export_phase2_part_3.py |
| TC-EXP-8405 | P1 | Manifest field databases with metadata 1 | field=databases,metadata=1 | present | test_export_phase2_part_3.py |
| TC-EXP-8406 | P1 | Manifest field databases with metadata 2 | field=databases,metadata=2 | present | test_export_phase2_part_3.py |
| TC-EXP-8407 | P1 | Manifest field databases with metadata 3 | field=databases,metadata=3 | present | test_export_phase2_part_3.py |
| TC-EXP-8408 | P1 | Manifest field databases with metadata 4 | field=databases,metadata=4 | present | test_export_phase2_part_3.py |
| TC-EXP-8409 | P1 | Manifest field databases with metadata 5 | field=databases,metadata=5 | present | test_export_phase2_part_3.py |
| TC-EXP-8410 | P1 | Manifest field databases with metadata 6 | field=databases,metadata=6 | present | test_export_phase2_part_3.py |
| TC-EXP-8411 | P1 | Manifest field databases with metadata 7 | field=databases,metadata=7 | present | test_export_phase2_part_3.py |
| TC-EXP-8412 | P1 | Manifest field databases with metadata 8 | field=databases,metadata=8 | present | test_export_phase2_part_3.py |
| TC-EXP-8413 | P1 | Manifest field databases with metadata 9 | field=databases,metadata=9 | present | test_export_phase2_part_3.py |
| TC-EXP-8414 | P1 | Manifest field databases with metadata 10 | field=databases,metadata=10 | present | test_export_phase2_part_3.py |
| TC-EXP-8415 | P1 | Manifest field databases with metadata 11 | field=databases,metadata=11 | present | test_export_phase2_part_3.py |
| TC-EXP-8416 | P1 | Manifest field databases with metadata 12 | field=databases,metadata=12 | present | test_export_phase2_part_3.py |
| TC-EXP-8417 | P1 | Manifest field notes with metadata 0 | field=notes,metadata=0 | present | test_export_phase2_part_3.py |
| TC-EXP-8418 | P1 | Manifest field notes with metadata 1 | field=notes,metadata=1 | present | test_export_phase2_part_3.py |
| TC-EXP-8419 | P1 | Manifest field notes with metadata 2 | field=notes,metadata=2 | present | test_export_phase2_part_3.py |
| TC-EXP-8420 | P1 | Manifest field notes with metadata 3 | field=notes,metadata=3 | present | test_export_phase2_part_3.py |
| TC-EXP-8421 | P1 | Manifest field notes with metadata 4 | field=notes,metadata=4 | present | test_export_phase2_part_3.py |
| TC-EXP-8422 | P1 | Manifest field notes with metadata 5 | field=notes,metadata=5 | present | test_export_phase2_part_3.py |
| TC-EXP-8423 | P1 | Manifest field notes with metadata 6 | field=notes,metadata=6 | present | test_export_phase2_part_3.py |
| TC-EXP-8424 | P1 | Manifest field notes with metadata 7 | field=notes,metadata=7 | present | test_export_phase2_part_3.py |
| TC-EXP-8425 | P1 | Manifest field notes with metadata 8 | field=notes,metadata=8 | present | test_export_phase2_part_3.py |
| TC-EXP-8426 | P1 | Manifest field notes with metadata 9 | field=notes,metadata=9 | present | test_export_phase2_part_3.py |
| TC-EXP-8427 | P1 | Manifest field notes with metadata 10 | field=notes,metadata=10 | present | test_export_phase2_part_3.py |
| TC-EXP-8428 | P1 | Manifest field notes with metadata 11 | field=notes,metadata=11 | present | test_export_phase2_part_4.py |
| TC-EXP-8429 | P1 | Manifest field notes with metadata 12 | field=notes,metadata=12 | present | test_export_phase2_part_4.py |
| TC-EXP-8430 | P1 | Manifest field schema_version with metadata 0 | field=schema_version,metadata=0 | present | test_export_phase2_part_4.py |
| TC-EXP-8431 | P1 | Manifest field schema_version with metadata 1 | field=schema_version,metadata=1 | present | test_export_phase2_part_4.py |
| TC-EXP-8432 | P1 | Manifest field schema_version with metadata 2 | field=schema_version,metadata=2 | present | test_export_phase2_part_4.py |
| TC-EXP-8433 | P1 | Manifest field schema_version with metadata 3 | field=schema_version,metadata=3 | present | test_export_phase2_part_4.py |
| TC-EXP-8434 | P1 | Manifest field schema_version with metadata 4 | field=schema_version,metadata=4 | present | test_export_phase2_part_4.py |
| TC-EXP-8435 | P1 | Manifest field schema_version with metadata 5 | field=schema_version,metadata=5 | present | test_export_phase2_part_4.py |
| TC-EXP-8436 | P1 | Manifest field schema_version with metadata 6 | field=schema_version,metadata=6 | present | test_export_phase2_part_4.py |
| TC-EXP-8437 | P1 | Manifest field schema_version with metadata 7 | field=schema_version,metadata=7 | present | test_export_phase2_part_4.py |
| TC-EXP-8438 | P1 | Manifest field schema_version with metadata 8 | field=schema_version,metadata=8 | present | test_export_phase2_part_4.py |
| TC-EXP-8439 | P1 | Manifest field schema_version with metadata 9 | field=schema_version,metadata=9 | present | test_export_phase2_part_4.py |
| TC-EXP-8440 | P1 | Manifest field schema_version with metadata 10 | field=schema_version,metadata=10 | present | test_export_phase2_part_4.py |
| TC-EXP-8441 | P1 | Manifest field schema_version with metadata 11 | field=schema_version,metadata=11 | present | test_export_phase2_part_4.py |
| TC-EXP-8442 | P1 | Manifest field schema_version with metadata 12 | field=schema_version,metadata=12 | present | test_export_phase2_part_4.py |
| TC-EXP-8443 | P1 | Manifest field detector_count with metadata 0 | field=detector_count,metadata=0 | present | test_export_phase2_part_4.py |
| TC-EXP-8444 | P1 | Manifest field detector_count with metadata 1 | field=detector_count,metadata=1 | present | test_export_phase2_part_4.py |
| TC-EXP-8445 | P1 | Manifest field detector_count with metadata 2 | field=detector_count,metadata=2 | present | test_export_phase2_part_4.py |
| TC-EXP-8446 | P1 | Manifest field detector_count with metadata 3 | field=detector_count,metadata=3 | present | test_export_phase2_part_4.py |
| TC-EXP-8447 | P1 | Manifest field detector_count with metadata 4 | field=detector_count,metadata=4 | present | test_export_phase2_part_4.py |
| TC-EXP-8448 | P1 | Manifest field detector_count with metadata 5 | field=detector_count,metadata=5 | present | test_export_phase2_part_4.py |
| TC-EXP-8449 | P1 | Manifest field detector_count with metadata 6 | field=detector_count,metadata=6 | present | test_export_phase2_part_4.py |
| TC-EXP-8450 | P1 | Manifest field detector_count with metadata 7 | field=detector_count,metadata=7 | present | test_export_phase2_part_4.py |
| TC-EXP-8451 | P1 | Manifest field detector_count with metadata 8 | field=detector_count,metadata=8 | present | test_export_phase2_part_4.py |
| TC-EXP-8452 | P1 | Manifest field detector_count with metadata 9 | field=detector_count,metadata=9 | present | test_export_phase2_part_4.py |
| TC-EXP-8453 | P1 | Manifest field detector_count with metadata 10 | field=detector_count,metadata=10 | present | test_export_phase2_part_4.py |
| TC-EXP-8454 | P1 | Manifest field detector_count with metadata 11 | field=detector_count,metadata=11 | present | test_export_phase2_part_4.py |
| TC-EXP-8455 | P1 | Manifest field detector_count with metadata 12 | field=detector_count,metadata=12 | present | test_export_phase2_part_4.py |
| TC-EXP-8456 | P1 | Manifest field ai_available with metadata 0 | field=ai_available,metadata=0 | present | test_export_phase2_part_4.py |
| TC-EXP-8457 | P1 | Manifest field ai_available with metadata 1 | field=ai_available,metadata=1 | present | test_export_phase2_part_4.py |
| TC-EXP-8458 | P1 | Manifest field ai_available with metadata 2 | field=ai_available,metadata=2 | present | test_export_phase2_part_4.py |
| TC-EXP-8459 | P1 | Manifest field ai_available with metadata 3 | field=ai_available,metadata=3 | present | test_export_phase2_part_4.py |
| TC-EXP-8460 | P1 | Manifest field ai_available with metadata 4 | field=ai_available,metadata=4 | present | test_export_phase2_part_4.py |
| TC-EXP-8461 | P1 | Manifest field ai_available with metadata 5 | field=ai_available,metadata=5 | present | test_export_phase2_part_4.py |
| TC-EXP-8462 | P1 | Manifest field ai_available with metadata 6 | field=ai_available,metadata=6 | present | test_export_phase2_part_4.py |
| TC-EXP-8463 | P1 | Manifest field ai_available with metadata 7 | field=ai_available,metadata=7 | present | test_export_phase2_part_4.py |
| TC-EXP-8464 | P1 | Manifest field ai_available with metadata 8 | field=ai_available,metadata=8 | present | test_export_phase2_part_4.py |
| TC-EXP-8465 | P1 | Manifest field ai_available with metadata 9 | field=ai_available,metadata=9 | present | test_export_phase2_part_4.py |
| TC-EXP-8466 | P1 | Manifest field ai_available with metadata 10 | field=ai_available,metadata=10 | present | test_export_phase2_part_4.py |
| TC-EXP-8467 | P1 | Manifest field ai_available with metadata 11 | field=ai_available,metadata=11 | present | test_export_phase2_part_4.py |
| TC-EXP-8468 | P1 | Manifest field ai_available with metadata 12 | field=ai_available,metadata=12 | present | test_export_phase2_part_4.py |
| TC-EXP-8469 | P1 | Manifest field semantic_available with metadata 0 | field=semantic_available,metadata=0 | present | test_export_phase2_part_4.py |
| TC-EXP-8470 | P1 | Manifest field semantic_available with metadata 1 | field=semantic_available,metadata=1 | present | test_export_phase2_part_4.py |
| TC-EXP-8471 | P1 | Manifest field semantic_available with metadata 2 | field=semantic_available,metadata=2 | present | test_export_phase2_part_4.py |
| TC-EXP-8472 | P1 | Manifest field semantic_available with metadata 3 | field=semantic_available,metadata=3 | present | test_export_phase2_part_4.py |
| TC-EXP-8473 | P1 | Manifest field semantic_available with metadata 4 | field=semantic_available,metadata=4 | present | test_export_phase2_part_4.py |
| TC-EXP-8474 | P1 | Manifest field semantic_available with metadata 5 | field=semantic_available,metadata=5 | present | test_export_phase2_part_4.py |
| TC-EXP-8475 | P1 | Manifest field semantic_available with metadata 6 | field=semantic_available,metadata=6 | present | test_export_phase2_part_4.py |
| TC-EXP-8476 | P1 | Manifest field semantic_available with metadata 7 | field=semantic_available,metadata=7 | present | test_export_phase2_part_4.py |
| TC-EXP-8477 | P1 | Manifest field semantic_available with metadata 8 | field=semantic_available,metadata=8 | present | test_export_phase2_part_4.py |
| TC-EXP-8482 | P2 | Retention 7d age 1d #0 | retention=7,age=1 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8483 | P2 | Retention 7d age 1d #1 | retention=7,age=1 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8484 | P2 | Retention 7d age 1d #2 | retention=7,age=1 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8485 | P2 | Retention 7d age 1d #3 | retention=7,age=1 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8486 | P2 | Retention 7d age 1d #4 | retention=7,age=1 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8487 | P2 | Retention 7d age 1d #5 | retention=7,age=1 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8488 | P2 | Retention 7d age 1d #6 | retention=7,age=1 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8489 | P2 | Retention 7d age 1d #7 | retention=7,age=1 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8490 | P2 | Retention 7d age 1d #8 | retention=7,age=1 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8491 | P2 | Retention 7d age 1d #9 | retention=7,age=1 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8492 | P2 | Retention 7d age 6d #0 | retention=7,age=6 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8493 | P2 | Retention 7d age 6d #1 | retention=7,age=6 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8494 | P2 | Retention 7d age 6d #2 | retention=7,age=6 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8495 | P2 | Retention 7d age 6d #3 | retention=7,age=6 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8496 | P2 | Retention 7d age 6d #4 | retention=7,age=6 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8497 | P2 | Retention 7d age 6d #5 | retention=7,age=6 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8498 | P2 | Retention 7d age 6d #6 | retention=7,age=6 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8499 | P2 | Retention 7d age 6d #7 | retention=7,age=6 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8500 | P2 | Retention 7d age 6d #8 | retention=7,age=6 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8501 | P2 | Retention 7d age 6d #9 | retention=7,age=6 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8502 | P2 | Retention 7d age 7d #0 | retention=7,age=7 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8503 | P2 | Retention 7d age 7d #1 | retention=7,age=7 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8504 | P2 | Retention 7d age 7d #2 | retention=7,age=7 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8505 | P2 | Retention 7d age 7d #3 | retention=7,age=7 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8506 | P2 | Retention 7d age 7d #4 | retention=7,age=7 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8507 | P2 | Retention 7d age 7d #5 | retention=7,age=7 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8508 | P2 | Retention 7d age 7d #6 | retention=7,age=7 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8509 | P2 | Retention 7d age 7d #7 | retention=7,age=7 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8510 | P2 | Retention 7d age 7d #8 | retention=7,age=7 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8511 | P2 | Retention 7d age 7d #9 | retention=7,age=7 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8512 | P2 | Retention 30d age 29d #0 | retention=30,age=29 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8513 | P2 | Retention 30d age 29d #1 | retention=30,age=29 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8514 | P2 | Retention 30d age 29d #2 | retention=30,age=29 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8515 | P2 | Retention 30d age 29d #3 | retention=30,age=29 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8516 | P2 | Retention 30d age 29d #4 | retention=30,age=29 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8517 | P2 | Retention 30d age 29d #5 | retention=30,age=29 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8518 | P2 | Retention 30d age 29d #6 | retention=30,age=29 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8519 | P2 | Retention 30d age 29d #7 | retention=30,age=29 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8520 | P2 | Retention 30d age 29d #8 | retention=30,age=29 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8521 | P2 | Retention 30d age 29d #9 | retention=30,age=29 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8522 | P2 | Retention 30d age 31d #0 | retention=30,age=31 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8523 | P2 | Retention 30d age 31d #1 | retention=30,age=31 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8524 | P2 | Retention 30d age 31d #2 | retention=30,age=31 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8525 | P2 | Retention 30d age 31d #3 | retention=30,age=31 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8526 | P2 | Retention 30d age 31d #4 | retention=30,age=31 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8527 | P2 | Retention 30d age 31d #5 | retention=30,age=31 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8528 | P2 | Retention 30d age 31d #6 | retention=30,age=31 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8529 | P2 | Retention 30d age 31d #7 | retention=30,age=31 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8530 | P2 | Retention 30d age 31d #8 | retention=30,age=31 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8531 | P2 | Retention 30d age 31d #9 | retention=30,age=31 | pruned correctly | test_export_phase2_part_4.py |
| TC-EXP-8532 | P2 | Retention 1d age 1d #0 | retention=1,age=1 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8533 | P2 | Retention 1d age 1d #1 | retention=1,age=1 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8534 | P2 | Retention 1d age 1d #2 | retention=1,age=1 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8535 | P2 | Retention 1d age 1d #3 | retention=1,age=1 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8536 | P2 | Retention 1d age 1d #4 | retention=1,age=1 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8537 | P2 | Retention 1d age 1d #5 | retention=1,age=1 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8538 | P2 | Retention 1d age 1d #6 | retention=1,age=1 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8539 | P2 | Retention 1d age 1d #7 | retention=1,age=1 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8540 | P2 | Retention 1d age 1d #8 | retention=1,age=1 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8541 | P2 | Retention 1d age 1d #9 | retention=1,age=1 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8542 | P2 | Retention 90d age 89d #0 | retention=90,age=89 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8543 | P2 | Retention 90d age 89d #1 | retention=90,age=89 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8544 | P2 | Retention 90d age 89d #2 | retention=90,age=89 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8545 | P2 | Retention 90d age 89d #3 | retention=90,age=89 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8546 | P2 | Retention 90d age 89d #4 | retention=90,age=89 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8547 | P2 | Retention 90d age 89d #5 | retention=90,age=89 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8548 | P2 | Retention 90d age 89d #6 | retention=90,age=89 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8549 | P2 | Retention 90d age 89d #7 | retention=90,age=89 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8550 | P2 | Retention 90d age 89d #8 | retention=90,age=89 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8551 | P2 | Retention 90d age 89d #9 | retention=90,age=89 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8552 | P2 | Retention 90d age 91d #0 | retention=90,age=91 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8553 | P2 | Retention 90d age 91d #1 | retention=90,age=91 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8554 | P2 | Retention 90d age 91d #2 | retention=90,age=91 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8555 | P2 | Retention 90d age 91d #3 | retention=90,age=91 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8556 | P2 | Retention 90d age 91d #4 | retention=90,age=91 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8557 | P2 | Retention 90d age 91d #5 | retention=90,age=91 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8558 | P2 | Retention 90d age 91d #6 | retention=90,age=91 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8559 | P2 | Retention 90d age 91d #7 | retention=90,age=91 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8560 | P2 | Retention 90d age 91d #8 | retention=90,age=91 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8561 | P2 | Retention 90d age 91d #9 | retention=90,age=91 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8562 | P2 | Retention 365d age 364d #0 | retention=365,age=364 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8563 | P2 | Retention 365d age 364d #1 | retention=365,age=364 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8564 | P2 | Retention 365d age 364d #2 | retention=365,age=364 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8565 | P2 | Retention 365d age 364d #3 | retention=365,age=364 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8566 | P2 | Retention 365d age 364d #4 | retention=365,age=364 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8567 | P2 | Retention 365d age 364d #5 | retention=365,age=364 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8568 | P2 | Retention 365d age 364d #6 | retention=365,age=364 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8569 | P2 | Retention 365d age 364d #7 | retention=365,age=364 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8570 | P2 | Retention 365d age 364d #8 | retention=365,age=364 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8571 | P2 | Retention 365d age 364d #9 | retention=365,age=364 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8572 | P2 | Retention 365d age 366d #0 | retention=365,age=366 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8573 | P2 | Retention 365d age 366d #1 | retention=365,age=366 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8574 | P2 | Retention 365d age 366d #2 | retention=365,age=366 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8575 | P2 | Retention 365d age 366d #3 | retention=365,age=366 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8576 | P2 | Retention 365d age 366d #4 | retention=365,age=366 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8577 | P2 | Retention 365d age 366d #5 | retention=365,age=366 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8578 | P2 | Retention 365d age 366d #6 | retention=365,age=366 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8579 | P2 | Retention 365d age 366d #7 | retention=365,age=366 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8580 | P2 | Retention 365d age 366d #8 | retention=365,age=366 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8581 | P2 | Retention 365d age 366d #9 | retention=365,age=366 | pruned correctly | test_export_phase2_part_5.py |
| TC-EXP-8582 | P2 | Multi-DB 1 tables 1 #0 | dbs=1,tables=1,scenario=0 | archived | test_export_phase2_part_5.py |
| TC-EXP-8583 | P2 | Multi-DB 1 tables 1 #1 | dbs=1,tables=1,scenario=1 | archived | test_export_phase2_part_5.py |
| TC-EXP-8584 | P2 | Multi-DB 1 tables 1 #2 | dbs=1,tables=1,scenario=2 | archived | test_export_phase2_part_5.py |
| TC-EXP-8585 | P2 | Multi-DB 1 tables 1 #3 | dbs=1,tables=1,scenario=3 | archived | test_export_phase2_part_5.py |
| TC-EXP-8586 | P2 | Multi-DB 1 tables 1 #4 | dbs=1,tables=1,scenario=4 | archived | test_export_phase2_part_5.py |
| TC-EXP-8587 | P2 | Multi-DB 1 tables 2 #0 | dbs=1,tables=2,scenario=0 | archived | test_export_phase2_part_5.py |
| TC-EXP-8588 | P2 | Multi-DB 1 tables 2 #1 | dbs=1,tables=2,scenario=1 | archived | test_export_phase2_part_5.py |
| TC-EXP-8589 | P2 | Multi-DB 1 tables 2 #2 | dbs=1,tables=2,scenario=2 | archived | test_export_phase2_part_5.py |
| TC-EXP-8590 | P2 | Multi-DB 1 tables 2 #3 | dbs=1,tables=2,scenario=3 | archived | test_export_phase2_part_5.py |
| TC-EXP-8591 | P2 | Multi-DB 1 tables 2 #4 | dbs=1,tables=2,scenario=4 | archived | test_export_phase2_part_5.py |
| TC-EXP-8592 | P2 | Multi-DB 1 tables 3 #0 | dbs=1,tables=3,scenario=0 | archived | test_export_phase2_part_5.py |
| TC-EXP-8593 | P2 | Multi-DB 1 tables 3 #1 | dbs=1,tables=3,scenario=1 | archived | test_export_phase2_part_5.py |
| TC-EXP-8594 | P2 | Multi-DB 1 tables 3 #2 | dbs=1,tables=3,scenario=2 | archived | test_export_phase2_part_5.py |
| TC-EXP-8595 | P2 | Multi-DB 1 tables 3 #3 | dbs=1,tables=3,scenario=3 | archived | test_export_phase2_part_5.py |
| TC-EXP-8596 | P2 | Multi-DB 1 tables 3 #4 | dbs=1,tables=3,scenario=4 | archived | test_export_phase2_part_5.py |
| TC-EXP-8597 | P2 | Multi-DB 1 tables 4 #0 | dbs=1,tables=4,scenario=0 | archived | test_export_phase2_part_5.py |
| TC-EXP-8598 | P2 | Multi-DB 1 tables 4 #1 | dbs=1,tables=4,scenario=1 | archived | test_export_phase2_part_5.py |
| TC-EXP-8599 | P2 | Multi-DB 1 tables 4 #2 | dbs=1,tables=4,scenario=2 | archived | test_export_phase2_part_5.py |
| TC-EXP-8600 | P2 | Multi-DB 1 tables 4 #3 | dbs=1,tables=4,scenario=3 | archived | test_export_phase2_part_5.py |
| TC-EXP-8601 | P2 | Multi-DB 1 tables 4 #4 | dbs=1,tables=4,scenario=4 | archived | test_export_phase2_part_5.py |
| TC-EXP-8602 | P2 | Multi-DB 2 tables 1 #0 | dbs=2,tables=1,scenario=0 | archived | test_export_phase2_part_5.py |
| TC-EXP-8603 | P2 | Multi-DB 2 tables 1 #1 | dbs=2,tables=1,scenario=1 | archived | test_export_phase2_part_5.py |
| TC-EXP-8604 | P2 | Multi-DB 2 tables 1 #2 | dbs=2,tables=1,scenario=2 | archived | test_export_phase2_part_5.py |
| TC-EXP-8605 | P2 | Multi-DB 2 tables 1 #3 | dbs=2,tables=1,scenario=3 | archived | test_export_phase2_part_5.py |
| TC-EXP-8606 | P2 | Multi-DB 2 tables 1 #4 | dbs=2,tables=1,scenario=4 | archived | test_export_phase2_part_5.py |
| TC-EXP-8607 | P2 | Multi-DB 2 tables 2 #0 | dbs=2,tables=2,scenario=0 | archived | test_export_phase2_part_5.py |
| TC-EXP-8608 | P2 | Multi-DB 2 tables 2 #1 | dbs=2,tables=2,scenario=1 | archived | test_export_phase2_part_5.py |
| TC-EXP-8609 | P2 | Multi-DB 2 tables 2 #2 | dbs=2,tables=2,scenario=2 | archived | test_export_phase2_part_5.py |
| TC-EXP-8610 | P2 | Multi-DB 2 tables 2 #3 | dbs=2,tables=2,scenario=3 | archived | test_export_phase2_part_5.py |
| TC-EXP-8611 | P2 | Multi-DB 2 tables 2 #4 | dbs=2,tables=2,scenario=4 | archived | test_export_phase2_part_5.py |
| TC-EXP-8612 | P2 | Multi-DB 2 tables 3 #0 | dbs=2,tables=3,scenario=0 | archived | test_export_phase2_part_5.py |
| TC-EXP-8613 | P2 | Multi-DB 2 tables 3 #1 | dbs=2,tables=3,scenario=1 | archived | test_export_phase2_part_5.py |
| TC-EXP-8614 | P2 | Multi-DB 2 tables 3 #2 | dbs=2,tables=3,scenario=2 | archived | test_export_phase2_part_5.py |
| TC-EXP-8615 | P2 | Multi-DB 2 tables 3 #3 | dbs=2,tables=3,scenario=3 | archived | test_export_phase2_part_5.py |
| TC-EXP-8616 | P2 | Multi-DB 2 tables 3 #4 | dbs=2,tables=3,scenario=4 | archived | test_export_phase2_part_5.py |
| TC-EXP-8617 | P2 | Multi-DB 2 tables 4 #0 | dbs=2,tables=4,scenario=0 | archived | test_export_phase2_part_5.py |
| TC-EXP-8618 | P2 | Multi-DB 2 tables 4 #1 | dbs=2,tables=4,scenario=1 | archived | test_export_phase2_part_5.py |
| TC-EXP-8619 | P2 | Multi-DB 2 tables 4 #2 | dbs=2,tables=4,scenario=2 | archived | test_export_phase2_part_5.py |
| TC-EXP-8620 | P2 | Multi-DB 2 tables 4 #3 | dbs=2,tables=4,scenario=3 | archived | test_export_phase2_part_5.py |
| TC-EXP-8621 | P2 | Multi-DB 2 tables 4 #4 | dbs=2,tables=4,scenario=4 | archived | test_export_phase2_part_5.py |
| TC-EXP-8622 | P2 | Multi-DB 3 tables 1 #0 | dbs=3,tables=1,scenario=0 | archived | test_export_phase2_part_5.py |
| TC-EXP-8623 | P2 | Multi-DB 3 tables 1 #1 | dbs=3,tables=1,scenario=1 | archived | test_export_phase2_part_5.py |
| TC-EXP-8624 | P2 | Multi-DB 3 tables 1 #2 | dbs=3,tables=1,scenario=2 | archived | test_export_phase2_part_5.py |
| TC-EXP-8625 | P2 | Multi-DB 3 tables 1 #3 | dbs=3,tables=1,scenario=3 | archived | test_export_phase2_part_5.py |
| TC-EXP-8626 | P2 | Multi-DB 3 tables 1 #4 | dbs=3,tables=1,scenario=4 | archived | test_export_phase2_part_5.py |
| TC-EXP-8627 | P2 | Multi-DB 3 tables 2 #0 | dbs=3,tables=2,scenario=0 | archived | test_export_phase2_part_5.py |
| TC-EXP-8628 | P2 | Multi-DB 3 tables 2 #1 | dbs=3,tables=2,scenario=1 | archived | test_export_phase2_part_5.py |
| TC-EXP-8629 | P2 | Multi-DB 3 tables 2 #2 | dbs=3,tables=2,scenario=2 | archived | test_export_phase2_part_5.py |
| TC-EXP-8630 | P2 | Multi-DB 3 tables 2 #3 | dbs=3,tables=2,scenario=3 | archived | test_export_phase2_part_5.py |
| TC-EXP-8631 | P2 | Multi-DB 3 tables 2 #4 | dbs=3,tables=2,scenario=4 | archived | test_export_phase2_part_5.py |
| TC-EXP-8632 | P2 | Multi-DB 3 tables 3 #0 | dbs=3,tables=3,scenario=0 | archived | test_export_phase2_part_6.py |
| TC-EXP-8633 | P2 | Multi-DB 3 tables 3 #1 | dbs=3,tables=3,scenario=1 | archived | test_export_phase2_part_6.py |
| TC-EXP-8634 | P2 | Multi-DB 3 tables 3 #2 | dbs=3,tables=3,scenario=2 | archived | test_export_phase2_part_6.py |
| TC-EXP-8635 | P2 | Multi-DB 3 tables 3 #3 | dbs=3,tables=3,scenario=3 | archived | test_export_phase2_part_6.py |
| TC-EXP-8636 | P2 | Multi-DB 3 tables 3 #4 | dbs=3,tables=3,scenario=4 | archived | test_export_phase2_part_6.py |
| TC-EXP-8637 | P2 | Multi-DB 3 tables 4 #0 | dbs=3,tables=4,scenario=0 | archived | test_export_phase2_part_6.py |
| TC-EXP-8638 | P2 | Multi-DB 3 tables 4 #1 | dbs=3,tables=4,scenario=1 | archived | test_export_phase2_part_6.py |
| TC-EXP-8639 | P2 | Multi-DB 3 tables 4 #2 | dbs=3,tables=4,scenario=2 | archived | test_export_phase2_part_6.py |
| TC-EXP-8640 | P2 | Multi-DB 3 tables 4 #3 | dbs=3,tables=4,scenario=3 | archived | test_export_phase2_part_6.py |
| TC-EXP-8641 | P2 | Multi-DB 3 tables 4 #4 | dbs=3,tables=4,scenario=4 | archived | test_export_phase2_part_6.py |
| TC-EXP-8642 | P2 | Multi-DB 4 tables 1 #0 | dbs=4,tables=1,scenario=0 | archived | test_export_phase2_part_6.py |
| TC-EXP-8643 | P2 | Multi-DB 4 tables 1 #1 | dbs=4,tables=1,scenario=1 | archived | test_export_phase2_part_6.py |
| TC-EXP-8644 | P2 | Multi-DB 4 tables 1 #2 | dbs=4,tables=1,scenario=2 | archived | test_export_phase2_part_6.py |
| TC-EXP-8645 | P2 | Multi-DB 4 tables 1 #3 | dbs=4,tables=1,scenario=3 | archived | test_export_phase2_part_6.py |
| TC-EXP-8646 | P2 | Multi-DB 4 tables 1 #4 | dbs=4,tables=1,scenario=4 | archived | test_export_phase2_part_6.py |
| TC-EXP-8647 | P2 | Multi-DB 4 tables 2 #0 | dbs=4,tables=2,scenario=0 | archived | test_export_phase2_part_6.py |
| TC-EXP-8648 | P2 | Multi-DB 4 tables 2 #1 | dbs=4,tables=2,scenario=1 | archived | test_export_phase2_part_6.py |
| TC-EXP-8649 | P2 | Multi-DB 4 tables 2 #2 | dbs=4,tables=2,scenario=2 | archived | test_export_phase2_part_6.py |
| TC-EXP-8650 | P2 | Multi-DB 4 tables 2 #3 | dbs=4,tables=2,scenario=3 | archived | test_export_phase2_part_6.py |
| TC-EXP-8651 | P2 | Multi-DB 4 tables 2 #4 | dbs=4,tables=2,scenario=4 | archived | test_export_phase2_part_6.py |
| TC-EXP-8652 | P2 | Multi-DB 4 tables 3 #0 | dbs=4,tables=3,scenario=0 | archived | test_export_phase2_part_6.py |
| TC-EXP-8653 | P2 | Multi-DB 4 tables 3 #1 | dbs=4,tables=3,scenario=1 | archived | test_export_phase2_part_6.py |
| TC-EXP-8654 | P2 | Multi-DB 4 tables 3 #2 | dbs=4,tables=3,scenario=2 | archived | test_export_phase2_part_6.py |
| TC-EXP-8655 | P2 | Multi-DB 4 tables 3 #3 | dbs=4,tables=3,scenario=3 | archived | test_export_phase2_part_6.py |
| TC-EXP-8656 | P2 | Multi-DB 4 tables 3 #4 | dbs=4,tables=3,scenario=4 | archived | test_export_phase2_part_6.py |
| TC-EXP-8657 | P2 | Multi-DB 4 tables 4 #0 | dbs=4,tables=4,scenario=0 | archived | test_export_phase2_part_6.py |
| TC-EXP-8658 | P2 | Multi-DB 4 tables 4 #1 | dbs=4,tables=4,scenario=1 | archived | test_export_phase2_part_6.py |
| TC-EXP-8659 | P2 | Multi-DB 4 tables 4 #2 | dbs=4,tables=4,scenario=2 | archived | test_export_phase2_part_6.py |
| TC-EXP-8660 | P2 | Multi-DB 4 tables 4 #3 | dbs=4,tables=4,scenario=3 | archived | test_export_phase2_part_6.py |
| TC-EXP-8661 | P2 | Multi-DB 4 tables 4 #4 | dbs=4,tables=4,scenario=4 | archived | test_export_phase2_part_6.py |
| TC-EXP-8662 | P2 | Multi-DB 5 tables 1 #0 | dbs=5,tables=1,scenario=0 | archived | test_export_phase2_part_6.py |
| TC-EXP-8663 | P2 | Multi-DB 5 tables 1 #1 | dbs=5,tables=1,scenario=1 | archived | test_export_phase2_part_6.py |
| TC-EXP-8664 | P2 | Multi-DB 5 tables 1 #2 | dbs=5,tables=1,scenario=2 | archived | test_export_phase2_part_6.py |
| TC-EXP-8665 | P2 | Multi-DB 5 tables 1 #3 | dbs=5,tables=1,scenario=3 | archived | test_export_phase2_part_6.py |
| TC-EXP-8666 | P2 | Multi-DB 5 tables 1 #4 | dbs=5,tables=1,scenario=4 | archived | test_export_phase2_part_6.py |
| TC-EXP-8667 | P2 | Multi-DB 5 tables 2 #0 | dbs=5,tables=2,scenario=0 | archived | test_export_phase2_part_6.py |
| TC-EXP-8668 | P2 | Multi-DB 5 tables 2 #1 | dbs=5,tables=2,scenario=1 | archived | test_export_phase2_part_6.py |
| TC-EXP-8669 | P2 | Multi-DB 5 tables 2 #2 | dbs=5,tables=2,scenario=2 | archived | test_export_phase2_part_6.py |
| TC-EXP-8670 | P2 | Multi-DB 5 tables 2 #3 | dbs=5,tables=2,scenario=3 | archived | test_export_phase2_part_6.py |
| TC-EXP-8671 | P2 | Multi-DB 5 tables 2 #4 | dbs=5,tables=2,scenario=4 | archived | test_export_phase2_part_6.py |
| TC-EXP-8672 | P2 | Multi-DB 5 tables 3 #0 | dbs=5,tables=3,scenario=0 | archived | test_export_phase2_part_6.py |
| TC-EXP-8673 | P2 | Multi-DB 5 tables 3 #1 | dbs=5,tables=3,scenario=1 | archived | test_export_phase2_part_6.py |
| TC-EXP-8674 | P2 | Multi-DB 5 tables 3 #2 | dbs=5,tables=3,scenario=2 | archived | test_export_phase2_part_6.py |
| TC-EXP-8675 | P2 | Multi-DB 5 tables 3 #3 | dbs=5,tables=3,scenario=3 | archived | test_export_phase2_part_6.py |
| TC-EXP-8676 | P2 | Multi-DB 5 tables 3 #4 | dbs=5,tables=3,scenario=4 | archived | test_export_phase2_part_6.py |
| TC-EXP-8677 | P2 | Multi-DB 5 tables 4 #0 | dbs=5,tables=4,scenario=0 | archived | test_export_phase2_part_6.py |
| TC-EXP-8678 | P2 | Multi-DB 5 tables 4 #1 | dbs=5,tables=4,scenario=1 | archived | test_export_phase2_part_6.py |
| TC-EXP-8679 | P2 | Multi-DB 5 tables 4 #2 | dbs=5,tables=4,scenario=2 | archived | test_export_phase2_part_6.py |
| TC-EXP-8680 | P2 | Multi-DB 5 tables 4 #3 | dbs=5,tables=4,scenario=3 | archived | test_export_phase2_part_6.py |
| TC-EXP-8681 | P2 | Multi-DB 5 tables 4 #4 | dbs=5,tables=4,scenario=4 | archived | test_export_phase2_part_6.py |
| TC-EXP-8682 | P3 | Export edge missing none | missing=none | handled | test_export_phase2_part_6.py |
| TC-EXP-8683 | P3 | Export edge missing data | missing=data | handled | test_export_phase2_part_6.py |
| TC-EXP-8684 | P3 | Export edge missing logs | missing=logs | handled | test_export_phase2_part_6.py |
| TC-EXP-8685 | P3 | Export edge missing data+logs | missing=data+logs | handled | test_export_phase2_part_6.py |
| TC-EXP-8686 | P3 | Export edge missing semantic | missing=semantic | handled | test_export_phase2_part_6.py |
| TC-EXP-8687 | P3 | Export edge missing data+semantic | missing=data+semantic | handled | test_export_phase2_part_6.py |
| TC-EXP-8688 | P3 | Export edge missing logs+semantic | missing=logs+semantic | handled | test_export_phase2_part_6.py |
| TC-EXP-8689 | P3 | Export edge missing data+logs+semantic | missing=data+logs+semantic | handled | test_export_phase2_part_6.py |
| TC-EXP-8690 | P3 | Export edge missing env | missing=env | handled | test_export_phase2_part_6.py |
| TC-EXP-8691 | P3 | Export edge missing data+env | missing=data+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8692 | P3 | Export edge missing logs+env | missing=logs+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8693 | P3 | Export edge missing data+logs+env | missing=data+logs+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8694 | P3 | Export edge missing semantic+env | missing=semantic+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8695 | P3 | Export edge missing data+semantic+env | missing=data+semantic+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8696 | P3 | Export edge missing logs+semantic+env | missing=logs+semantic+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8697 | P3 | Export edge missing data+logs+semantic+env | missing=data+logs+semantic+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8698 | P3 | Export edge missing example | missing=example | handled | test_export_phase2_part_6.py |
| TC-EXP-8699 | P3 | Export edge missing data+example | missing=data+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8700 | P3 | Export edge missing logs+example | missing=logs+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8701 | P3 | Export edge missing data+logs+example | missing=data+logs+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8702 | P3 | Export edge missing semantic+example | missing=semantic+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8703 | P3 | Export edge missing data+semantic+example | missing=data+semantic+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8704 | P3 | Export edge missing logs+semantic+example | missing=logs+semantic+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8705 | P3 | Export edge missing data+logs+semantic+example | missing=data+logs+semantic+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8706 | P3 | Export edge missing env+example | missing=env+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8707 | P3 | Export edge missing data+env+example | missing=data+env+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8708 | P3 | Export edge missing logs+env+example | missing=logs+env+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8709 | P3 | Export edge missing data+logs+env+example | missing=data+logs+env+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8710 | P3 | Export edge missing semantic+env+example | missing=semantic+env+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8711 | P3 | Export edge missing data+semantic+env+example | missing=data+semantic+env+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8712 | P3 | Export edge missing logs+semantic+env+example | missing=logs+semantic+env+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8713 | P3 | Export edge missing data+logs+semantic+env+example | missing=data+logs+semantic+env+example | handled | test_export_phase2_part_6.py |
| TC-EXP-8714 | P3 | Export edge missing none | missing=none | handled | test_export_phase2_part_6.py |
| TC-EXP-8715 | P3 | Export edge missing data | missing=data | handled | test_export_phase2_part_6.py |
| TC-EXP-8716 | P3 | Export edge missing logs | missing=logs | handled | test_export_phase2_part_6.py |
| TC-EXP-8717 | P3 | Export edge missing data+logs | missing=data+logs | handled | test_export_phase2_part_6.py |
| TC-EXP-8718 | P3 | Export edge missing semantic | missing=semantic | handled | test_export_phase2_part_6.py |
| TC-EXP-8719 | P3 | Export edge missing data+semantic | missing=data+semantic | handled | test_export_phase2_part_6.py |
| TC-EXP-8720 | P3 | Export edge missing logs+semantic | missing=logs+semantic | handled | test_export_phase2_part_6.py |
| TC-EXP-8721 | P3 | Export edge missing data+logs+semantic | missing=data+logs+semantic | handled | test_export_phase2_part_6.py |
| TC-EXP-8722 | P3 | Export edge missing env | missing=env | handled | test_export_phase2_part_6.py |
| TC-EXP-8723 | P3 | Export edge missing data+env | missing=data+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8724 | P3 | Export edge missing logs+env | missing=logs+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8725 | P3 | Export edge missing data+logs+env | missing=data+logs+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8726 | P3 | Export edge missing semantic+env | missing=semantic+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8727 | P3 | Export edge missing data+semantic+env | missing=data+semantic+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8728 | P3 | Export edge missing logs+semantic+env | missing=logs+semantic+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8729 | P3 | Export edge missing data+logs+semantic+env | missing=data+logs+semantic+env | handled | test_export_phase2_part_6.py |
| TC-EXP-8730 | P3 | Export edge missing example | missing=example | handled | test_export_phase2_part_6.py |
| TC-EXP-8731 | P3 | Export edge missing data+example | missing=data+example | handled | test_export_phase2_part_6.py |

### Phase 3 - 15,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-EXP-0671 onward.

### Phase 4 - 150,000 cases
- Planned high-scale scenarios, IDs TC-EXP-15671 onward.

### Phase 5 - 1,334,330 cases
- Planned exhaustive dimension sweep, IDs TC-EXP-165671 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_export_phase2_part_1.py | 8124-8223 | P1 | :white_check_mark: Phase 2 |
| test_export_phase2_part_2.py | 8224-8327 | P1 | :white_check_mark: Phase 2 |
| test_export_phase2_part_3.py | 8328-8427 | P2 | :white_check_mark: Phase 2 |
| test_export_phase2_part_4.py | 8428-8531 | P1 | :white_check_mark: Phase 2 |
| test_export_phase2_part_5.py | 8532-8631 | P2 | :white_check_mark: Phase 2 |
| test_export_phase2_part_6.py | 8632-8731 | P2 | :white_check_mark: Phase 2 |

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
- Data Export
