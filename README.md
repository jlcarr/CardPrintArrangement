# CardPrintArrangement
A Python script to aid in arranging playing cards for printing.

## Usage
1. Ensure you have 2 .png files for each card (1 for the front, 1 for the back)
2. Ensure all these files are named according to the **File Naming** section below
3. Place all these files into the *inputs* directory
4. Execute the script ```python3 PrintPlacement.py```
5. Check *outputs* directory for the results

### File Naming
{#}_{card_name}{front/back}.png
- **Format**: .png (Cards should be in PNG format for losslessness)
- **#**: The card number in ordering
- **card_name**: This can contain any text which helps identify the card
- **front/back**: This is an empty string "" if it is the card front. If it is the back fill with "[back]".
#### Example
- 1_firstcard.png
- 1_firstcard[back].png
- 2_secondcard.png
- 2_secondcard[back].png

### Configuration
The config.json file should be edited to reflect the print job desired. In particular the following fields are needed.
- **printsheet-height-inches**: The height (vertical direction) of the sheets upon which the cards with be printed in inches.
- **printsheet-width-inches**: The width (horizontal direction) of the sheets upon which the cards with be printed in inches.
- **printsheet-ppi**: The pixels per inch (ppi) of the images generated for printing.
- **card-height-inches**: The heigth (vertical direction) of the cards to be printed and cut out.
- **card-width-inches**: The width (horizontal direction) of the cards to be printed and cut out.
- **card-bleed-inches**: The vertical and horizontal bleed (additional image margin added to account for cutting error tolerances) for the card images in inches.
#### Example
```json
{
	"printsheet-height-inches": 11, 
	"printsheet-width-inches": 8.5,
	"printsheet-ppi": 300,
	"card-height-inches": 3.5,
	"card-width-inches": 2.25,
	"card-bleed-inches": 0.125
}
```
