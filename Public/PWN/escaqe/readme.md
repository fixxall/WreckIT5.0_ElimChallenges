
challenge_name: escaqe

challenge_description: CAKE ORRRRR FAKE

challenge_flag: WRECKIT50{FAKE_cuz_0day_or_misconf_w4s_th3r3_and_shellcoding_sux}

challenge_participant_file: participant-escaqe.zip

challenge connection:
-file_transfer: nc HOST 7125
-qemu: nc HOST 7126

challenge backup connection:
-file_transfer: nc 103.152.118.120 7125
-qemu: nc 103.152.118.120 7126

build server commands:
cd docker; docker-compose up -d --build
