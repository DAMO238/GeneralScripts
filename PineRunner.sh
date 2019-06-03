#!/bin/sh

read -sp 'Password: ' p
tmux new-session -d -s 'Sanjeev'
#sleep 10; tmux new-window -n 'Disc Emote Reply' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 DISC.py '$p'"
#sleep 10; tmux new-window -n 'Disc Emote Static' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 EmoteStatic.py '$p'"
#sleep 10; tmux new-window -n 'Rocket Emote Static' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 RocketEmoteStatic.py '$p'"
sleep 10; tmux new-window -n 'Random Reactions' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 RandomReact2.py '$p'"
sleep 10; tmux new-window -n 'Colour Changer' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 RandomColours.py '$p'"
sleep 10; tmux new-window -n 'Sanjeev Replier' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 SanjeevReply.py '$p'"
sleep 10; tmux new-window -n 'Poll Interacter' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 Polling.py '$p'"
sleep 10; tmux new-window -n 'Rocket Meeting Reminder' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 ReminderRocket.py '$p'"
sleep 10; tmux new-window -n 'Fealty Detector' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 fealtyDetector.py '$p'"
sleep 10; tmux new-window -n 'Stop Detector' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 StopDetector.py '$p'"
sleep 10; tmux new-window -n "Sanjeev's Inspiration" -c '/home/sanjeev/sanjeevscripts/fb/' "python3 SanjeevInspiration.py '$p'"
sleep 10; tmux new-window -n 'Secretary Sanjeev' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 SecretarySanjeev.py '$p'"
sleep 10; tmux new-window -n 'Playful Sanjeev' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 FizzBuzzSanjeev.py '$p'"
sleep 10; tmux new-window -n 'Spelling Sanjeev' -c '/home/sanjeev/sanjeevscripts/fb/' "python3 SpellingSanjeev.py '$p'"
