" markdown bindings

" italic
    nnoremap <C-i> wbi*<esc>ea*<esc>h
    vnoremap <silent> <C-i> :s/\%V.*\%V/\*\0\*<CR>:nohl<CR><C-l>``f*

" bold
    nnoremap <C-b> wbi**<esc>ea**<esc>hh
    vnoremap <silent> <C-b> :s/\%V.*\%V/\*\*\0\*\*<CR>:nohl<CR><C-l>``3f*

" superscript
    nnoremap <C-k> wbi<sup><esc>ea</sup><esc>F<h
    vnoremap <silent> <C-k> :s/\%V.*\%V/<sup>\0<\/sup><CR>:nohl<CR><C-l>``2f>

" subscript
    nnoremap <C-j> wbi<sub><esc>ea</sub><esc>F<h
    vnoremap <silent> <C-j> :s/\%V.*\%V/<sub>\0<\/sub><CR>:nohl<CR><C-l>``2f>
