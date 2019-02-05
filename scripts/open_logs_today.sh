echo 'Opening your life logs for today!'

  nvim -O2 ~/Documents/notes/life/$(date +%y%m%d).txt ~/Documents/notes/dev/$(date +%y%m%d).txt 

  echo 'Have a good day!'
