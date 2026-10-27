default exorcism = None

default approach_points = {
    "compassion": 0.
    "procedure": 0,
    "curiosity": 0,
    "pragmatism": 0,
    "improvisation": 0,
}

init python: 
    CASES = {

    }

    APPROACHES = {
        "compassion",
        "procedure",
        "curiosity",
        "pragmatism",
        "improvisation"
    }

    TOOLS = {
        "emf" :{
            "name": "EMF Meter",
            "description" : "A tool that measures local disturbances in electromagnetic fields. Readings can vary by room and can change over time."
            "uses": None
        },

        "spirit_box" : {
            "name": "Spirit Box",
            "description": "A tool that cycles through radio frequenies, attempting real-time communication with unstable ghosts. Clarity depends on the ghost's cohesion, power, and well, willingness.",
            "uses": None
        },

        "charm": {
            "name": "Stabilization Charm",
            "description": "A talisman that temporarily steadies a ghost's cohesion. It doesn't last long, however.",
            "uses": 2
        },

        "seal": {
            "name": "Containment Seal",
            "description": "A talisman that restricts a manifestation or ghost. Should be a last resort tool. All seals are sent to the MMD rehabilitation center once inhabited.",
            "uses": 1
        },

        "salt": {
            "name": "Table Salt",
            "description": "Good ol' sodium chloride. Use it to lay a temporary boundary line.",
            "uses" : 3
        }
    }

    ## EXORCISM SETUP
    def begin_exorcism(case_id):
        """Start a new exorcism session. Call from a label."""
        case = CASES[case_id]

        store.exorcism = {
            "case_id": case_id,

            "room": case["start_room"],

            "tools": {},

            "carried": [],

            "journal": {
                "observations": [],
                "accounts": [],
                "explanations": [],
            },

            "ghost": dict(case.get("ghost_start", {})),
            "flags": [],

            "actions": 0,
            "charm_left": 0,
            "emf_override": {},

            "emf_seen": {},
            "events_fired": [],
            "clues": [],

            "diagnosis_id": None,
            "intervention": None,
            "report_answers": [],

        }

    def exorcism_case():
        return CASES[exorcism["case_id"]]

    def room_data(): 
        return exorcism_case()["rooms"][exorcism["room"]]

    ## TOOLS
    def exorcism_equip(tool_id): 
        exorcism["tools"][tool_id] = TOOLS[tool_id].get("uses", None)

    def exorcism_has_tool(tool_id):
        return tool_id in exorcism["tools"]

    def exorcism_consume(tool_id):
        if not exorcism_has_tool(tool_id):
            return False

        left = exorcism["tools"][tool_id]

        if left is None:
            return True

        if left > 0:
            exo["tools"][tool_id] = left - 1
            return True

        return False

    ## CARRIED ITEMS, FLAGS, AND CLUES
    def exorcism_carry(item_id):
        if item_id not in exorcism["carried"]:
            exorcism["carried"].append(item_id)

    def exorcism_flag(name):
        return name in exorcism["flags"]

    def exorcism_set_flag(name):
        if name not in exo["flags"]:
            exorcism["flags"].append(name)

    def exorcism_once(flag_name):

        if exorcism_flag(flag_name):
            return False
        exo_set_flag(flag_name)
        return True

    def exorcism_clue(clue_id):
        if clue_id not in exorcism["clues"]:
            exorcism["clues"].append(clue_id)

    def exorcism_clue_count():
        return len(exorcism["clues"])

    def exorcism_clue_has(clue_id):
        return clue_id in exorcism["clues"]

    def exorcism_diagnosis():
        diag_id = exorcism.get("diagnosis_id")

        if diag_id is None:
            return None

        for option in exorcism_case()["diagnoses"]:
            if option["id"] == diag_id:
                return option

        return None

    ## JOURNAL
    def exorcism_observations(text):
        if text not in exorcism["journal"]["observations"]:
            exorcism["journal"]["observations"].append(text)

    def exorcism_accounts(text):
        if text not in exorcism["journal"]["accounts"]:
            exorcism["journal"]["accounts"].append(text)

    def exorcism_explanations(text):
        if text not in exorcism["journal"]["explanations"]:
            exorcism["journal"]["explanations"].append(text)
