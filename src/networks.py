# Main network and testnet3 definitions

# Polis src/chainparams.cpp
params = {
    'polis_main': {
        'pubkey_address': 55, #L120
        'script_address': 56, #L122
        'genesis_hash': '000009701eb781a8113b1af1d814e2f060f6408a2c990db291bc5108a1345c1e' #L110
    },
    'polis_test': {
        'pubkey_address': 140, #L220
        'script_address': 19, #L222
        'genesis_hash': '0000009038aeaea86784e959b0b4002793adad39fc9d6f8789ed2edf99ad5c8b' #L210
    }
}
