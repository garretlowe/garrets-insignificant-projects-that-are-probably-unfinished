/* Garret Lowe 2022 */

const ROUTES = {
  "road": {},
  "boat": {
    "Dagon Fel": {
      "Khuul": {
        "travel_time": 8,
        "gold_cost": 0
      },
      "Sadrith Mora": {
        "travel_time": 10,
        "gold_cost": 0
      },
      "Tel Aruhn": {
        "travel_time": 9,
        "gold_cost": 0
      },
      "Tel Mora": {
        "travel_time": 5,
        "gold_cost": 0
      }
    },
    "Ebonheart": {
      "Hla Oad": {
        "travel_time": 5,
        "gold_cost": 0
      },
      "Holamayan": {
        "travel_time": 9,
        "gold_cost": 0
      },
      "Sadrith Mora": {
        "travel_time": 11,
        "gold_cost": 0
      },
      "Tel Branora": {
        "travel_time": 6,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 1,
        "gold_cost": 0
      }
    },
    "Gnaar Mok": {
      "Hla Oad": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Khuul": {
        "travel_time": 7,
        "gold_cost": 0
      }
    },
    "Hla Oad": {
      "Ebonheart": {
        "travel_time": 5,
        "gold_cost": 0
      },
      "Gnaar Mok": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Molag Mar": {
        "travel_time": 10,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 5,
        "gold_cost": 0
      }
    },
    "Holamayan": {
      "Ebonheart": {
        "travel_time": 9,
        "gold_cost": 0
      }
    },
    "Khuul": {
      "Dagon Fel": {
        "travel_time": 8,
        "gold_cost": 0
      },
      "Gnaar Mok": {
        "travel_time": 7,
        "gold_cost": 0
      }
    },
    "Molag Mar": {
      "Hla Oad": {
        "travel_time": 10,
        "gold_cost": 0
      },
      "Tel Branora": {
        "travel_time": 2,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 4,
        "gold_cost": 0
      }
    },
    "Sadrith Mora": {
      "Dagon Fel": {
        "travel_time": 10,
        "gold_cost": 0
      },
      "Ebonheart": {
        "travel_time": 11,
        "gold_cost": 0
      },
      "Tel Branora": {
        "travel_time": 8,
        "gold_cost": 0
      },
      "Tel Mora": {
        "travel_time": 5,
        "gold_cost": 0
      }
    },
    "Tel Aruhn": {
      "Dagon Fel": {
        "travel_time": 9,
        "gold_cost": 0
      },
      "Tel Mora": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Vos": {
        "travel_time": 4,
        "gold_cost": 0
      }
    },
    "Tel Branora": {
      "Ebonheart": {
        "travel_time": 6,
        "gold_cost": 0
      },
      "Molag Mar": {
        "travel_time": 2,
        "gold_cost": 0
      },
      "Sadrith Mora": {
        "travel_time": 8,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 5,
        "gold_cost": 0
      }
    },
    "Tel Mora": {
      "Dagon Fel": {
        "travel_time": 5,
        "gold_cost": 0
      },
      "Sadrith Mora": {
        "travel_time": 5,
        "gold_cost": 0
      },
      "Tel Aruhn": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Vos": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Vivec": {
      "Ebonheart": {
        "travel_time": 1,
        "gold_cost": 0
      },
      "Hla Oad": {
        "travel_time": 5,
        "gold_cost": 0
      },
      "Molag Mar": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Tel Branora": {
        "travel_time": 5,
        "gold_cost": 0
      }
    },
    "Vos": {
      "Sadrith Mora": {
        "travel_time": 5,
        "gold_cost": 0
      },
      "Tel Aruhn": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Tel Mora": {
        "travel_time": 0,
        "gold_cost": 0
      }
    }
  },
  "silt_strider": {
    "Ald'ruhn": {
      "Balmora": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Gnisis": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Khuul": {
        "travel_time": 5,
        "gold_cost": 0
      },
      "Maar Gan": {
        "travel_time": 2,
        "gold_cost": 0
      }
    },
    "Balmora": {
      "Ald'ruhn": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Seyda Neen": {
        "travel_time": 3,
        "gold_cost": 0
      },
      "Suran": {
        "travel_time": 5,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 4,
        "gold_cost": 0
      }
    },
    "Gnisis": {
      "Ald'ruhn": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Khuul": {
        "travel_time": 3,
        "gold_cost": 0
      },
      "Maar Gan": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Seyda Neen": {
        "travel_time": 11,
        "gold_cost": 0
      }
    },
    "Khuul": {
      "Ald'ruhn": {
        "travel_time": 5,
        "gold_cost": 0
      },
      "Gnisis": {
        "travel_time": 3,
        "gold_cost": 0
      },
      "Maar Gan": {
        "travel_time": 3,
        "gold_cost": 0
      }
    },
    "Maar Gan": {
      "Ald'ruhn": {
        "travel_time": 2,
        "gold_cost": 0
      },
      "Gnisis": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Khuul": {
        "travel_time": 3,
        "gold_cost": 0
      }
    },
    "Molag Mar": {
      "Suran": {
        "travel_time": 3,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 4,
        "gold_cost": 0
      }
    },
    "Seyda Neen": {
      "Balmora": {
        "travel_time": 3,
        "gold_cost": 0
      },
      "Gnisis": {
        "travel_time": 11,
        "gold_cost": 0
      },
      "Suran": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 2,
        "gold_cost": 0
      }
    },
    "Suran": {
      "Balmora": {
        "travel_time": 5,
        "gold_cost": 0
      },
      "Molag Mar": {
        "travel_time": 3,
        "gold_cost": 0
      },
      "Seyda Neen": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 1,
        "gold_cost": 0
      }
    },
    "Vivec": {
      "Balmora": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Molag Mar": {
        "travel_time": 4,
        "gold_cost": 0
      },
      "Seyda Neen": {
        "travel_time": 2,
        "gold_cost": 0
      },
      "Suran": {
        "travel_time": 1,
        "gold_cost": 0
      }
    }
  },
  "mage_guild": {
    "Ald'ruhn": {
      "Balmora": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Sadrith Mora": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Balmora": {
      "Ald'ruhn": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Sadrith Mora": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Caldera": {
      "Ald'ruhn": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Balmora": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Sadrith Mora": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Sadrith Mora": {
      "Ald'ruhn": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Balmora": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Vivec": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Vivec": {
      "Ald'ruhn": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Balmora": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Sadrith Mora": {
        "travel_time": 0,
        "gold_cost": 0
      }
    }
  },
  "propylon": {
    "Andasreth": {
      "Berandas": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Hlormaren": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Berandas": {
      "Andasreth": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Falasmaryon": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Falasmaryon": {
      "Berandas": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Valenvaryon": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Falensarano": {
      "Indoranyon": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Telasero": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Hlormaren": {
      "Andasreth": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Marandus": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Indoranyon": {
      "Falensarano": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Rotheran": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Marandus": {
      "Hlormaren": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Telasero": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Rotheran": {
      "Indoranyon": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Valenvaryon": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Telasero": {
      "Falensarano": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Marandus": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Valenvaryon": {
      "Falasmaryon": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Rotheran": {
        "travel_time": 0,
        "gold_cost": 0
      }
    }
  },
  "master_propylon": {
    "Andasreth": {
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Berandas": {
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Caldera": {
      "Andasreth": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Berandas": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Falasmaryon": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Falensarano": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Hlormaren": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Indoranyon": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Marandus": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Rotheran": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Telasero": {
        "travel_time": 0,
        "gold_cost": 0
      },
      "Valenvaryon": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Falasmaryon": {
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Falensarano": {
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Hlormaren": {
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Indoranyon": {
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Marandus": {
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Rotheran": {
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Telasero": {
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Valenvaryon": {
      "Caldera": {
        "travel_time": 0,
        "gold_cost": 0
      }
    }
  },
  "dlc": {
    "Ebonheart": {
      "Mournhold": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Fort Frostmoth": {
      "Khuul": {
        "travel_time": 6,
        "gold_cost": 0
      },
      "Raven Rock": {
        "travel_time": 2,
        "gold_cost": 0
      }
    },
	"Khuul": {
      "Fort Frostmoth": {
        "travel_time": 6,
        "gold_cost": 0
      }
	},
    "Mournhold": {
      "Ebonheart": {
        "travel_time": 0,
        "gold_cost": 0
      }
    },
    "Raven Rock": {
      "Fort Frostmoth": {
        "travel_time": 2,
        "gold_cost": 0
      }
    }
  }
};

const LOCATIONS = {
    "Ald'ruhn": {
        "location_type": "city",
        "road": true,
        "boat": false,
        "silt_strider": true,
        "mage_guild": true,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Balmora": {
        "location_type": "city",
        "road": true,
        "boat": false,
        "silt_strider": true,
        "mage_guild": true,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Sadrith Mora": {
        "location_type": "city",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": true,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Vivec": {
        "location_type": "city",
        "road": true,
        "boat": true,
        "silt_strider": true,
        "mage_guild": true,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Ald Velothi": {
        "location_type": "town",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Caldera": {
        "location_type": "town",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": true,
        "propylon": true,
        "master_propylon": true,
		"dlc": false
    },
    "Dagon Fel": {
        "location_type": "town",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Gnaar Mok": {
        "location_type": "town",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Gnisis": {
        "location_type": "town",
        "road": true,
        "boat": false,
        "silt_strider": true,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Hla Oad": {
        "location_type": "town",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Khuul": {
        "location_type": "town",
        "road": true,
        "boat": true,
        "silt_strider": true,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": true
    },
    "Maar Gan": {
        "location_type": "town",
        "road": true,
        "boat": false,
        "silt_strider": true,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Molag Mar": {
        "location_type": "town",
        "road": true,
        "boat": true,
        "silt_strider": true,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Pelagiad": {
        "location_type": "town",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Seyda Neen": {
        "location_type": "town",
        "road": true,
        "boat": false,
        "silt_strider": true,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Skaal Village": {
        "location_type": "town",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Suran": {
        "location_type": "town",
        "road": true,
        "boat": false,
        "silt_strider": true,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Tel Aruhn": {
        "location_type": "town",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Tel Branora": {
        "location_type": "town",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Tel Fyr": {
        "location_type": "town",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Tel Mora": {
        "location_type": "town",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Tel Vos": {
        "location_type": "town",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Vos": {
        "location_type": "town",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Indarys Manor": {
        "location_type": "house_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Rethan Manor": {
        "location_type": "house_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Tel Uvirith": {
        "location_type": "house_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Buckmoth Legion For": {
        "location_type": "imperial_fort",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Ebonheart": {
        "location_type": "imperial_fort",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": true
    },
    "Moonmoth Imperial Fort": {
        "location_type": "imperial_fort",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Wolverine Hall": {
        "location_type": "imperial_fort",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Ahemmusa Camp": {
        "location_type": "major_camp",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Erabenimsun Camp": {
        "location_type": "major_camp",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Urshilaku Camp": {
        "location_type": "major_camp",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Zainab Camp": {
        "location_type": "major_camp",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Andasreth": {
        "location_type": "dunmer_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": true,
        "master_propylon": true,
		"dlc": false
    },
    "Berandas": {
        "location_type": "dunmer_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": true,
        "master_propylon": true,
		"dlc": false
    },
    "Falasmaryon": {
        "location_type": "dunmer_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": true,
        "master_propylon": true,
		"dlc": false
    },
    "Falensarano": {
        "location_type": "dunmer_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": true,
        "master_propylon": true,
		"dlc": false
    },
    "Hlormaren": {
        "location_type": "dunmer_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": true,
        "master_propylon": true,
		"dlc": false
    },
    "Indoranyon": {
        "location_type": "dunmer_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": true,
        "master_propylon": true,
		"dlc": false
    },
    "Kogoruhn": {
        "location_type": "dunmer_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Marandus": {
        "location_type": "dunmer_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": true,
        "master_propylon": true,
		"dlc": false
    },
    "Rotheran": {
        "location_type": "dunmer_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": true,
		"master_propylon": true,
		"dlc": false
    },
    "Telasero": {
        "location_type": "dunmer_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": true,
        "master_propylon": true,
		"dlc": false
    },
    "Valenvaryon": {
        "location_type": "dunmer_stronghold",
        "road": true,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": true,
        "master_propylon": true,
		"dlc": false
    },
    "Holamayan": {
        "location_type": "temple",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    }
};

const DLC_LOCATIONS = {
    "Fort Firemoth": {
        "location_type": "imperial_fort",
        "road": false,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Fort Frostmoth": {
        "location_type": "imperial_fort",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    },
    "Mournhold": {
        "location_type": "city",
        "road": false,
        "boat": false,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": true
    },
    "Raven Rock": {
        "location_type": "town",
        "road": true,
        "boat": true,
        "silt_strider": false,
        "mage_guild": false,
        "propylon": false,
        "master_propylon": false,
		"dlc": false
    }
};
