import csv
from pathlib import Path
from typing import List

modes_csv_path = Path("./GameModes.csv")
contents = modes_csv_path.read_text()

reader = csv.reader(contents.splitlines())
header_row = []
rows: List[str] = []
for i, line in enumerate(reader):
    if i == 0:
        header_row = line
    else:
        rows.append(line)



def insert_col_if_missing(name, index):
    if len(header_row) >= index or name != header_row[index]:
        header_row.insert(index, name)
        for row in rows:
            row.insert(index, "")

insert_col_if_missing("RoyalStars", 21)


def set_opts_for_mode(mode_name, opts):
    ix = header_row.index(mode_name)
    if ix < 1:
        raise Exception(f"Unknown mode: {mode_name}")
    added = set()
    for row in rows:
        if row[0] in opts:
            row[ix] = '1'
            added.add(row[0])
    missing = set(opts) - added
    if len(missing) > 0:
        m2 = list(missing)
        m2.sort()
        print(f"\n !! Missing Settings: {m2}\m")
    for opt in missing:
        new_row = [opt] + ['']*(len(header_row) - 1)
        new_row[ix] = '1'
        rows.append(new_row)

royal_opts = [
    "S_ChatTime",
"S_UseClublinks",
"S_UseClublinksSponsors",
"S_NeutralEmblemUrl",
"S_ScriptEnvironment",
"S_IsChannelServer",
"S_DelayBeforeNextMap",
"S_RespawnBehaviour",
"S_ForceLapsNb",
"S_InfiniteLaps",
"S_EnableJoinLeaveNotifications",
"S_SeasonIds",
"S_IsSplitScreen",
"S_DecoImageUrl_WhoAmIUrl",
"S_DecoImageUrl_Checkpoint",
"S_DecoImageUrl_DecalSponsor4x1",
"S_DecoImageUrl_Screen16x9",
"S_DecoImageUrl_Screen8x1",
"S_DecoImageUrl_Screen16x1",
"S_ClubId",
"S_ClubName",
"S_LoadingScreenImageUrl",
"S_TrustClientSimu",
"S_UseCrudeExtrapolation",
"S_SynchronizePlayersAtMapStart",
"S_DisableGoToMap",
"S_PickAndBan_Enable",
"S_PickAndBan_Style",
"S_TimeLimit",
"S_SegmentBonusTime",
"S_SegmentRecordPoints",
"S_StarsNbToUnlockNextSegment",
"S_StarsReward_First",
"S_StarsReward_Record",
"S_StarsReward_Gold",
"S_StarsReward_Silver",
"S_StarsReward_Bronze",
"S_StarsTimeRatio_Gold",
"S_StarsTimeRatio_Silver",
"S_MatchWaitingScreenDuration",
"S_RoundWaitingScreenDuration",
"S_IsMatchmaking",
"S_MatchId",
"S_ClanStyle",
"S_AddBotsUntil",
"S_MaxBotsTeams",
"S_MinBotLevel",
"S_MaxBotLevel",
"S_EnableGhostsUpload",
"S_GhostDBId",
"S_IsSuperRoyal",
"S_SuperRoyalRoundNumber",
"S_IsSuperRoyalFinale",
"S_Division",
"S_OnlyFirstGetPoints",
]


set_opts_for_mode("RoyalStars", royal_opts)

def gen_csv():
    all_rows = [header_row] + rows
    all_rows.sort()
    return '\n'.join([','.join(row) for row in all_rows])

print(gen_csv())
modes_csv_path.write_text(gen_csv())
