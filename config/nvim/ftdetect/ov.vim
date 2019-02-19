"au BufRead,BufNewFile *.ovm setfiletype ovm

" my filetype file
" if exists("did_load_filetypes")
"   finish
" endif
augroup filetypedetect
  au! BufRead,BufNewFile *.ovm		setfiletype ovm
  au! BufRead,BufNewFile *.ovf		setfiletype ovm
  au! BufRead,BufNewFile *.ovt		setfiletype ovm
augroup END

" au Syntax ovm	    runtime! ~/.vim/syntax/ovm.vim
" au Syntax ovt	    runtime! $VIMRUNTIME/syntax/c.vim
" au Syntax ovf	    runtime! $VIMRUNTIME/syntax/c.vim

" au BufRead,BufNewFile *.ovm syn match sql /"\zsCLASS\w*\ze"/ 
" au BufRead,BufNewFile *.ovm hi sql guifg=white guibg=red ctermfg=white ctermbg=red
" au BufRead,BufNewFile *.ovm syn match ovInclude /^\s*\zs\(%:\|#\)\s*include\>\s*["<]/ 
" au BufRead,BufNewFile *.ovm hi ovInclude guifg=white guibg=red ctermfg=white ctermbg=red
" display contains=ovIncluded    links to Include

