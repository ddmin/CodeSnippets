# Tabbed

## Run
```console
tabbed -c alacritty --embed
```

## Makefile
```console
# Uncomment this for the alpha patch / ALPHA_PATCH
LDFLAGS = -lXrender
```

```console
# if make file doesn't work
cp patches.def.h patches.h
```

## Building
```console
git clone https://github.com/bakkeby/tabbed-flexipatch
make
sudo make install
```

## Manually Patching
patch -p0 < patch.diff
