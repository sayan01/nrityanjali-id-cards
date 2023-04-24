# nrityanjali-id-cards
Shell scripts and python scripts to automate the creation of id cards for both participants and organizers of nrityanjali.

Organizer's cards and scripts are present in `organizers/` and participants cards and scripts are present in `participants/`.

To generate cards run `./genid` in the respective folder.

The `list` file needs to have the data in TSV format.

The `./genqr` script is auto-run but can also be run manually to generate the QR code for each participant.

To remove preexisting images run `rm id/*.png` in the respective folder.

# Procedure
- Populate `list` with ids
- Run `./genid` create id cards
- Run `./merge` to merge them into 3x3 A3 sheets

Copyright - Sayan - 2023
