# CardPrintArrangement
A Python script to aid in arranging playing cards for printing.

## Usage
1. Ensure you have 2 .png files for each card (1 for the front, 1 for the back)
2. Ensure all these files are named according to the *File Naming* section below
3. Place all these files into the *inputs* directory
4. Execute the script ```python3 PrintPlacement.py```
5. Check *outputs* directory for the results

### File Naming
{#}_{card_name}{front/back}.png
- **Format**: .png (Cards should be in PNG format for losslessness)
- **#**: The card number in ordering
- **card_name**: This can contain any text which helps identify the card
- **front/back**: This is an empty string "" if it is the card front. If it is the back fill with "[back]".
