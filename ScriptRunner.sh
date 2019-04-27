#!/bin/sh
read -sp 'Password: ' p
echo $p
gnome-terminal --tab --title='Group Message' --command='sh -c "python3 JohnGroupAuto.py '$p'" $SHELL'
gnome-terminal --tab --title='Disc Emote Reply' --command='sh -c "python3 DISC.py '$p'"'
gnome-terminal --tab --title='Disc Emote Static' --command='sh -c "python3 EmoteStatic.py '$p'"'
gnome-terminal --tab --title='Rocket Emote Static' --command='sh -c "python3 RocketEmoteStatic.py '$p'"'
gnome-terminal --tab --title='Random Reactions' --command='sh -c "python3 RandomReact2.py '$p'"'
gnome-terminal --tab --title='Colour Changer' --command='sh -c "python3 RandomColours.py '$p'"'
gnome-terminal --tab --title='Sanjeev Replier' --command='sh -c "python3 SanjeevReply.py '$p'"'
gnome-terminal --tab --title='Poll Interacter' --command='sh -c "python3 Polling.py '$p'"'
gnome-terminal --tab --title='Rocket Meeting Reminder' --command='sh -c "python3 ReminderRocket.py '$p'"'
gnome-terminal --tab --title='Fealty Detector' --command='sh -c "python3 fealtyDetector.py '$p'"'
gnome-terminal --tab --title='Stop Detector' --command='sh -c "python3 StopDetector.py '$p'"'
gnome-terminal --tab --title="Sanjeev's Inspiration" --command='sh -c "python3 SanjeevInspiration.py '$p'"'
gnome-terminal --tab --title='Secretary Sanjeev' --command='sh -c "python3 SecretarySanjeev.py '$p'"'
gnome-terminal --tab --title='Playful Sanjeev' --command='sh -c "python3 FizzBuzzSanjeev.py '$p'"'
gnome-termianl --tab --title='Spelling Sanjeev' --command='sh -c "python3 SpellingSanjeev.py '$p'"'
gnome-terminal --tab --title='AI Visualisation' --command='cmatrix'
clear

