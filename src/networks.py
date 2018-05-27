# Main network and testnet3 definitions

# Seci src/chainparams.cpp
params = {
    'seci_main': {
        'pubkey_address': 63, #L120
        'script_address': 5, #L122
        'genesis_hash': '00000d2e96a48dbbc13255fcfa039a61cf8511567d861543010c0bab630e0018' #L110
    },
    'seci_test': {
        'pubkey_address': 127, #L220
        'script_address': 19, #L222
        'genesis_hash': '00000dbd0851f08eb802e0e822c9475512c04b402f9040b0d7b6bfd1b1356033' #L210
    }
}
