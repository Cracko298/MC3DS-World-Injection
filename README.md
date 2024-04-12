# MC3DS-World-Injection
### Better Known as "Festive World Override"
An exploit that allows for index.cdb to be read and not checked for validity. Allowing custom made Maps to be played without inputting extra save data.

## How it Works:
1. **A template index.cdb was used in creating the exploit, used a few parts of it to trick the Game into loading it while retaining some of the World Data I wanted (LoCity in this Case).**
2. **The file "<ins>template.json</ins>" was then modified to include randomly generated structures from LoCity and weird terrain.**
3. **Slot/Chunk Data (<ins>slt.cdb</ins>) files where just brought over from the default map, and referenced in "<ins>template.json</ins>". Allowing for Random Generation from the index file.**
4. **Blang/LOC Files where modified using '[mc3dslib](https://github.com/Cracko298/mc3dslib)'. And a custom Python Script (provided in "<ins>.\src\python</ins>" on GitHub).**
5. **The Panorama Images where originally made by [@STBrian](https://github.com/STBrian). And where downloaded via his Personal UniStore.**
6. Some new structures are also randomly generated, thanks to OliverDISC for his Map LoCity.

## Mod Screenshots:
![2018-07-22_15-24-37 116_top](https://github.com/Cracko298/MC3DS-World-Injection/assets/78656905/bd8fec52-535c-42de-926c-a9629c50c234)
![2018-07-22_15-24-14 465_top](https://github.com/Cracko298/MC3DS-World-Injection/assets/78656905/2f0b4c1c-a643-47ee-988c-ff2ec30d9cbd)
![2018-07-22_15-23-49 697_top](https://github.com/Cracko298/MC3DS-World-Injection/assets/78656905/afe7b7ac-8046-49fe-ae7c-52410d14fbf5)
![2018-07-22_14-51-15 490_top](https://github.com/Cracko298/MC3DS-World-Injection/assets/78656905/63599b75-c1c3-4b1b-a851-85722cb1b7f1)
![2018-07-22_15-25-08 657_bot](https://github.com/Cracko298/MC3DS-World-Injection/assets/78656905/5e4b5470-0189-4a29-8903-7390e9c1af16)
![2018-07-22_15-25-04 331_bot](https://github.com/Cracko298/MC3DS-World-Injection/assets/78656905/4675f0f6-7d5b-4f94-ac7d-c584b3e28fec)
![2018-07-22_15-24-57 884_bot](https://github.com/Cracko298/MC3DS-World-Injection/assets/78656905/03fd8d40-be9b-4c2a-ba69-f2611f7db39b)
