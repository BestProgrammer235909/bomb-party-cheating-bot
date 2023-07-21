# bomb-party-cheating-bot
## TLDR
This is a programme that helps one cheat in the web game Bomb Party. 
## Context
Bomb Party is an online word game where players connect adjacent letters to form words within a time limit. The goal is to avoid losing lives by creating as many valid words as possible. It is important to note that one can get an extra life by having used every letter of the alphabet, assuming a maximum number of lives isn't hit. Additionally, the same word cannot be used twice. Bomb Party supposedly enhances vocabulary and critical thinking skills.
## Use
One should start the programme in command prompt, adjusting the window such that the supposed bomb party room is visible. The programme prompts the user to press enter, and upon the user pressing enter, the command prompt window is minimised, and the letter prompt being displayed on the bomb party website is selected and copied. The programme then types a suitable word into the bomb party answer box before entering it. This word will always be the shortest possible word, in order to prevent suspicion being aroused from the bombparty community. It will also always use at least one new letter of the alphabet (if possible), making it drastically easier to get extra lives. The command prompt window is then opened again in the aforementioned window position. 
To use this programme to cheat, one should press enter every time it is their turn to enter a word.
## Limitations
- The programme occasionally fails to produce a word, resulting in the user having to manually input a word, before restarting the programme in command prompt. This can not only cause the player to lose a life (or a round) from exceeding time limits or having no responses, it also resets the list of words and alphabets used, making it more likely for the programme to return ineffective or invalid responses when it is restarted.
  - To work around this, we should use `try: ` `except: ` blocks such that the programme doesn't need to be restarted.
  - For a long-term fix, we should find a more suitable dictionary of words for the programme to iterate through, such that the programme doesn't fail to produce responses.
- The programme can occasionally return invalid responses, usually when said response has already been entered by another user.
  - There is no clear fix for this. When the problem occurs, the user must manually write a suitable word themselves. This can not only cause them to lose a life (or a round)  from exceeding time limits or having no responses, it also throws off the list of words and alphabets used, making it more likely for the programme to return ineffective or invalid responses when it is restarted. We could possibly keep track of words used by other users through the BombParty API, but since documentation on this isn't accessible, it is more practical to just compromise the effectiveness of the programme and accept this as a limitation.
- The programme is only usable on laptop/pc, as it requires command prompt. This results in mobile/tablet users being unable to use this programme.
  - We could potentially write a version of the programme that is usable on mobile/tablet. This will be difficult without the use of non-web-based IDEs, as the programme heavily relies on PyAutoGui.
    
