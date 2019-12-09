
# Introduction
This repository contain scripts I have made for [mpv media player](https://github.com/mpv-player/mpv/). To add scripts from this repository, download the desired script in your `mpv/scripts/` directory (click [here](https://mpv.io/manual/master/#lua-scripting) to know more about mpv scripts).

**This repository contain the following scripts:**
- [**SmartCopyPaste Script**](https://github.com/Eisa01/mpv-scripts#smartcopypaste-script)
- [**SmartCopyPaste-II Script**](https://github.com/Eisa01/mpv-scripts#smartcopypaste-ii-script)
- [**SmartHistory Script**](https://github.com/Eisa01/mpv-scripts#smarthistory-script)
- [**SimpleUndo Script**](https://github.com/Eisa01/mpv-scripts#simpleundo-script)
- [**UndoRedo Script**](https://github.com/Eisa01/mpv-scripts#undoredo-script)

**The following scripts can conflict with each other:**
- Either install SmartCopyPaste or SmartCopyPaste-II.
- Either install SimpleUndo or UndoRedo.
# SmartCopyPaste Script
SmartCopyPaste is a script for mpv media player, the script adds a very smart copy paste experience to mpv. It gives mpv the ability to load videos simply by pasting them into mpv. As for copying,  pressing <kbd>ctrl</kbd>+<kbd>c</kbd> on a video, copies the video path and its time to clipboard, which enables paste to resume or to access video with the copied time by pasting. For installation, download *`SmartCopyPaste.lua`* file into your `mpv/scripts/` directory. 
### SmartCopyPaste Main Features
- **Copy and Paste**: Adds ability to copy and paste any type of video to mpv, like (urls, video paths, or local videos)
- **youtube-dl Extension Support** Immediately paste links without finding exact video address for youtube and any other youtube-dl extension supported sites.
- **OSD** (On Screen Display): Displays any SmartCopyPaste action within mpv.
### SmartCopyPaste Usage Guide
**While running a video:**
- <kbd>ctrl</kbd>+<kbd>c</kbd> to copy video path with resume time
- *<kbd>ctrl</kbd>+<kbd>v</kbd> does the following:*
	- To jump to the copied time
	- Or when different video is copied, <kbd>ctrl</kbd>+<kbd>v</kbd> will add it into playlist
- <kbd>ctrl</kbd>+<kbd>**C**</kbd> to copy video path without resume time
- <kbd>ctrl</kbd>+<kbd>**V**</kbd> to add video into playlist to play it next

**While `NOT` running a video:**
- <kbd>ctrl</kbd>+<kbd>v</kbd> to play the copied video with resume time _if available_
### SmartCopyPaste Compatibility
- Currently for Windows OS only.
# SmartCopyPaste-II Script
SmartCopyPaste is a script for mpv media player, the script adds a very smart copy paste experience to mpv. It gives mpv the ability to load videos simply by pasting them into mpv. As for copying,  pressing <kbd>ctrl</kbd>+<kbd>c</kbd> on a video, copies the video path and its time to clipboard, which enables paste to resume or to access video with the copied time by pasting. 
The **II** version contain additional features which saves your clipboard into a log file. The log adds the option to paste at any time even if clipboard was overwritten or cleared. 

Basically,  the **II**  version is enhanced with a bookmark feature, copying a video will bookmark the video and time, while pasting will access the bookmark (even if clipboard is cleared). For installation, download *`SmartCopyPaste-II.lua`* file into your `mpv/scripts/` directory. 
### SmartCopyPaste-II Main Features
- **Copy and Paste**: Adds ability to copy and paste any type of video to mpv, like (urls, video paths, or local videos)
- **Bookmark**: Any copy in a video is also a bookmark point, to access the bookmark simply paste.
- **Save Clipboard to a Log File:** The copies from mpv, and the pastes into mpv will be kept in a log file located in `%APPDATA%\mpv\mpvClipboard.log`. This is necessary for the bookmark feature.
- **youtube-dl Extension Support** Immediately paste links without finding exact video address for youtube and any other youtube-dl extension supported sites.
- **OSD**: Displays any SmartCopyPaste action within mpv.
### SmartCopyPaste-II Usage Guide
**While running a video:**
- <kbd>ctrl</kbd>+<kbd>c</kbd> to copy video path with resume time and bookmark it
- *<kbd>ctrl</kbd>+<kbd>v</kbd> does the following:*
	- To jump to the copied time
	- Or to jump to the bookmarked position in the bookmarked video (resume)
- <kbd>ctrl</kbd>+<kbd>**C**</kbd> to copy video path without resume time and bookmark
- <kbd>ctrl</kbd>+<kbd>**V**</kbd> to add video into playlist to play it next
	
**While `NOT` running a video:**
- *<kbd>ctrl</kbd>+<kbd>v</kbd> does the following:*
	- To play the copied video with resume time _if available_
	- Or when no video is currently copied, <kbd>ctrl</kbd>+<kbd>v</kbd> will find and play your last copied or pasted video
- <kbd>ctrl</kbd>+<kbd>c</kbd> to access your videos clipboard history
### SmartCopyPaste-II Compatibility
- Currently for Windows OS only.
# SmartHistory Script
SmartHistory is a script for mpv media player, the script adds a smart history functionality to mpv. It logs videos that you opened into `%APPDATA%\mpv\mpvHistory.log` along with the time you have reached on each video. The script uses the log to provide you with various features. More details about SmartHistory are explained in the sections below. For installation, download *`SmartHistory.lua`* file into your `mpv/scripts/` directory. 
### SmartHistory Main Features
- **Remember Last Video:** It will always remember your last played video, and <kbd>ctrl</kbd>+<kbd>l</kbd> will jump to your last played video.
- **Auto Bookmark:** When you exit video, it will always remember position and <kbd>ctrl</kbd>+<kbd>r</kbd> will resume. 
-  **Logs Opened Videos to a Log File:** All videos opened in mpv will be logged to create a history in `%APPDATA%\mpv\mpvHistory.log`. The format is: [date and time] of accessing video, the path & reached video time. This is necessary for Remember Last Video and Auto Bookmark.
- **OSD**: Displays any SmartHistory action within mpv.
### SmartHistory Usage Guide
**While running a video:**
- <kbd>ctrl</kbd>+<kbd>l</kbd> to immediately load last closed video 
- <kbd>ctrl</kbd>+<kbd>r</kbd> to open history log for list of played videos
	- Use this along with SmartCopyPaste script to copy and paste video from history log into mpv

**While `NOT` running a video:**
- <kbd>ctrl</kbd>+<kbd>r</kbd> to resume in any previously closed videos
- <kbd>ctrl</kbd>+<kbd>l</kbd> to add previously closed video into playlist  
	- Useful for cases when you opened another video by accident and you want to get back to the last video
### SmartHistory Compatibility
 - Currently for Windows OS only.
# SimpleUndo Script
SimpleUndo is a script for mpv media player, the script adds a simple undo functionality into mpv. If you accidentally seek/jump to a different time in the video, press undo <kbd>ctrl</kbd>+<kbd>z</kbd> to return to your previous time and vice-versa. For installation, download *`SimpleUndo.lua`* file into your `mpv/scripts/` directory. 
### SimpleUndo Main Features
- **Simple Undo**: Undo accidental time jumps in videos by pressing <kbd>ctrl</kbd>+<kbd>z</kbd> and press again to return to previous position.
- **OSD**: Displays any SimpleUndo action within mpv.
### SimpleUndo Usage Guide
- <kbd>ctrl</kbd>+<kbd>z</kbd> to undo accidental seek by returning to previous time and vise-versa.
### SimpleUndo Compatibility
- Should work on all of mpv supported platforms.
# UndoRedo Script
UndoRedo is a script for mpv media player, the script adds undo, and redo functionality into mpv. If you seek/jump to a different time in the video, press undo <kbd>ctrl</kbd>+<kbd>z</kbd> to linearly undo the seeks/jumps in the video, and press redo <kbd>ctrl</kbd>+<kbd>y</kbd> to linearly return to previous undo positions. For installation, download *`UndoRedo.lua`* file into your `mpv/scripts/` directory. 
### UndoRedo Main Features
- **Undo and Redo**: Undo any accident time jumps in the video by pressing <kbd>ctrl</kbd>+<kbd>z</kbd> and redo the jumps by <kbd>ctrl</kbd>+<kbd>y</kbd>.
- **Simple Undo**: : Undo accidental time jumps in videos by pressing <kbd>ctrl</kbd>+<kbd>z</kbd> and press again to return to previous position.
- **OSD**: Displays any SimpleUndo action within mpv.
### UndoRedo Usage Guide
- <kbd>ctrl</kbd>+<kbd>z</kbd> to undo by returning to previous times. 
	- Example: from second 30 jumped to minute 5, then 10, then 15. Undo will return to 10, undo again to return to 5, undo again to return to second 30.
- <kbd>ctrl</kbd>+<kbd>y</kbd> to redo by restoring undo times. 
	- Example: from second 30 jumped to minute 5, then 10. Undo twice for second 30. Redo will restore to 5, redo again to restore to 10.
- <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>z</kbd> loop between last undo and redo.
	- This is for quick undo & redo (Just like **SimpleUndo**) it loops between the last undo & redo.
### UndoRedo Compatibility
 - Should work on all of mpv supported platforms.
# Misc
### To-Do List
- Support more platforms for scripts that are currently Windows OS only
- I am open to suggestions! Have an idea... let me know.. ;)
### Changelog
- [Here](https://github.com/Eisa01/mpv-scripts/blob/master/.doc/changelog.md) you can find the full changelog for all the scripts in this repository.
### Special Thanks
Below is list of contributors/ honorable mentions.
- **SmartCopyPaste Script** 
To access windows clipboard, the method was inspired by [@wiiaboo](https://github.com/wiiaboo/) urlcopypaste script. Special thanks for his work.
- **SmartHistory Script**
To create the log file, the method was inspired by a deleted author from a reddit post. Special thanks for his work.
- **UndoRedo Script**
Credits and special thanks to [@Banz99](https://github.com/Banz99) for forking SimpleUndo script and enhance it by a table to store undo and redo values, as well as iterate between them. Also special thanks for his full explanation on how it works.
