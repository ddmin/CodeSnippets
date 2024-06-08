" Vim syntax file for Badly Managed Kollections (BMK) files

if exists("b:current_syntax")
    finish
endif

let b:current_syntax = "lst"

" Manually Remove Comments (not prefixed with):
"                           ^, #, @, !, ^, ~
syn match   pln              "^[^#@!^~].*"

" Title Prefix Characters
" `, ~, !, @, #, $, %, ^, &, *, _, -, +, =, ?
syn match   ttlpfx contained "^#\zs[`~!@#\$%\^&*_\-+=\?]"
syn match   ttl              "^#.*" contains=ttlpfx

syn match   pfx              "^\^.*"
syn match   glpfx            "^\~.*"

syn match   lnk              "^@.*"
syn match   desc             "^!.*$" contains=tg
syn match   tg contained     "\[.\{-}\]" contains=tgtext
syn match   tgtext contained "[^[\]]*"

hi def link ttl      Constant
hi def link ttlpfx   Error
hi def link pfx      CursorColumn
hi def link glpfx    Error
hi def link lnk      Comment
hi def link pln      CursorLine
hi def link tg       PreProc
hi def link tgtext   Statement
hi def link desc     PreProc
