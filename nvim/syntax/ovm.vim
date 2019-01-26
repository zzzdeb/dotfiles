" Vim syntax file
" Language:	ovm
" Maintainer:	Zolboo Erdenebayar <zolboo.deb@gmail.com>
" Last Change:	

" Quit when a (custom) syntax file was already loaded
if exists("b:current_syntax")
  finish
endif

let s:cpo_save = &cpo
set cpo&vim

let s:ft = matchstr(&ft, '^\([^.]\)\+')

  so $VIMRUNTIME/syntax/c.vim

  syn keyword	ovType		BOOL INT UINT SINGLE DOUBLE TIME TIME_SPAN STRING BOOL_PV INT_PV UINT_PV SINGLE_PV DOUBLE_PV STRING_PV TIME_PV TIME_SPAN_PV ANY 
  syn keyword	ovWords		LIBRARY END_LIBRARY STRUCTUR END_STRUCTUR CLASS VARIABLES END_VARIABLES OPERATIONS END_OPERATIONS PARTS END_PARTS END_CLASS ASSOCIATION PARENT CHILD END_ASSOCIATION C_TYPE UNIT C_FUNCTION FLAGS INITIALVALUE IS_INSTANTIABLE IS_FINAL IS_LOCAL HAS_GET_ACCESSOR HAS_SET_ACCESSOR HAS_ACCESSORS IS_DERIVED IS_STATIC IS_ABSTRACT ONE_TO_ONE ONE_TO_MANY MANY_TO_MANY OV_AT_MANY_TO_MANY
  syn keyword	ovTailbar	VERSION AUTHOR COPYRIGHT COMMENT 
  

hi def link ovType		Type
hi def link ovWords		Type
hi def link ovTailbar		Type

let b:current_syntax = "ovm"

unlet s:ft

let &cpo = s:cpo_save
unlet s:cpo_save
" vim: ts=8
