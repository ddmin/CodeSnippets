" Vim syntax file for Badly Managed Kollections (BMK) files

if exists("b:current_syntax")
    finish
endif

let b:current_syntax = "lst"

syn match   ttl              "^#.*"
syn match   lnk              "^@.*"
syn match   pln              "^[^#@!].*"

syn match   desc             "^!.*$" contains=tg
syn match   tg contained     "\[.\{-}\]" contains=tgtext
syn match   tgtext contained "[^[\]]*"

hi def link ttl      Constant
hi def link lnk      Comment
hi def link pln      Normal
hi def link tg       PreProc
hi def link tgtext   Statement
hi def link desc     PreProc
