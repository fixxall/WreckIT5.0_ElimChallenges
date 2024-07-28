
challenge_name: butamap

challenge_description: SUPPORT KOK PUSH SENDIRIAN? SUPPORTNYA TEMPLATEEEE

challenge_flag: WRECKIT50{blind_ptmx_ret2usr_is_based}

challenge_participant_file: not provided

challenge connection:
-qemu: nc HOST 16968

challenge backup connection:
-qemu: nc 103.152.118.120 16968

build server commands:
cd server; docker-compose up -d --build
