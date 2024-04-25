Garage Door Controller with Raspberry Pi Pico W

This project transforms a Raspberry Pi Pico W into a WiFi-enabled garage door controller, allowing remote operation through a simple web interface. The web interface is also optimized as a Progressive Web Application (PWA), making it installable on mobile devices for convenient access.

Features:
- Remote Operation: Control your garage door remotely using the provided web interface.
- Progressive Web App: Add the controller to your home screen on iOS or Android for easy access, thanks to the integrated PWA support.
- Visual Feedback: A clear and user-friendly HTML interface displays the current state of the door and allows for intuitive control.

Setup:
- Upload the Icon: Ensure icon.png is uploaded to your Raspberry Pi Pico W. This icon is used for the PWA manifest and should be placed in the root directory.
- WiFi Configuration: Update the ssid and password variables with your WiFi network details to enable internet connectivity.
- Web Interface Access: Access the web interface by navigating to the Raspberry Pi Pico W's IP address on your browser. You can find the IP address printed on the console upon successful connection to WiFi.

Web Server Details:
- Manifest and Icons: The manifest JSON is dynamically served to support the PWA functionality, allowing device-specific optimizations like icons and theme colors.
- Home Dashboard Button: A dedicated button on the web interface redirects to a home automation dashboard (change the IP address in the HTML code to match your setup).

Code Modifications:
- The original script was modified to enhance functionality and user experience, including better HTML structure and additional PWA support.

Acknowledgements:
- Original script concept by Michael at Core Electronics. This version has been extended to include additional features and improvements for personal use and ease of integration into home automation systems. @ https://core-electronics.com.au/projects/wifi-garage-door-controller-with-raspberry-pi-pico-w-smart-home-project/

Screenshots:
- Below are some screenshots demonstrating the PWA in action, illustrating the interface and its features on a mobile device.


![Screenshot_20240422_203246_Chrome](https://github.com/MrLately/garage_door/assets/94589563/dcc14640-c507-46e5-8a30-2688434d2199)
![Screenshot_20240422_203428_One UI Home](https://github.com/MrLately/garage_door/assets/94589563/8f5f21ca-5e21-4ac2-8537-7ccd8308c147)
![Screenshot_20240422_204106_Gallery](https://github.com/MrLately/garage_door/assets/94589563/0f08d5bf-0a27-4aa9-959d-1aeeb444d82b)
![Screenshot_20240422_203303_Chrome](https://github.com/MrLately/garage_door/assets/94589563/f8348ed1-f861-4f88-9551-845eb148c701)
