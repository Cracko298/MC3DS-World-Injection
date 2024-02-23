# MC3DS-World-Injection
An exploit that allows for index.cdb to be read and not checked for validity. Allowing custom made Maps to be played without inputting extra save data.

## How it Works:
1. **A template index.cdb was used in creating the exploit, used a few parts of it to trick the Game into loading it while retaining some of the World Data I wanted (LoCity in this Case).**
2. **The file "<ins>template.json</ins>" was then modified to include randomly generated structures from LoCity and weird terrain.**
3. **Slot/Chunk Data (<ins>slt.cdb</ins>) files where just brought over from the default map, and referenced in "<ins>template.json</ins>". Allowing for Random Generation from the index file.**
4. **Blang/LOC Files where modified using '[mc3dslib](https://github.com/Cracko298/mc3dslib)'. And a custom Python Script (provided in ".\src\python" on GitHub).**
5. **The Panorama Images where originally made by [@STBrian](https://github.com/STBrian). And where downloaded via his Personal UniStore.**
