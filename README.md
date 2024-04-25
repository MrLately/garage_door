i uploaded icon.png via thonny through files/upload to.

import ujson as json. could of just used ujson but already put json in the function and I'm lazy.

there is a function to serve the manifest but could have possibly put an actual manifest.json but figured micropython is best left micro.

added this into the html portion: 
    \\\<link rel="manifest" href="/manifest.json">

in the loop is if manifest.json... elif image... continue.

this is for the pwa. when you afd to homesceen on ios or android it requests manifest json so this is how i serve it.

original script from Michael @ https://core-electronics.com.au/projects/wifi-garage-door-controller-with-raspberry-pi-pico-w-smart-home-project/

i also added and a home dashboard button but thats for my use case. if you use it change the ip to match.
also cleaned the look of html portion for readability.

![Screenshot_20240422_203246_Chrome](https://github.com/MrLately/garage_door/assets/94589563/dcc14640-c507-46e5-8a30-2688434d2199)
![Screenshot_20240422_203428_One UI Home](https://github.com/MrLately/garage_door/assets/94589563/8f5f21ca-5e21-4ac2-8537-7ccd8308c147)
![Screenshot_20240422_204106_Gallery](https://github.com/MrLately/garage_door/assets/94589563/0f08d5bf-0a27-4aa9-959d-1aeeb444d82b)
![Screenshot_20240422_203303_Chrome](https://github.com/MrLately/garage_door/assets/94589563/f8348ed1-f861-4f88-9551-845eb148c701)
