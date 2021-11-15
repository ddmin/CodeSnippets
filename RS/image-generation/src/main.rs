use std::fs::File;
use std::io::prelude::*;

#[derive(Clone)]
struct Size {
    width: u64,
    height: u64,
}

struct ImageFile {
    file: File,
    size: Size,
}

fn create_ppm(name: &str, size: Size) -> ImageFile {
    let header = format!("P3\n{} {} 255\n", size.width, size.height);
    let mut f = File::create(name).unwrap();
    f.write(header.as_bytes()).unwrap();
    ImageFile { file: f, size }
}

fn solid(f: &mut ImageFile) {
    println!("Creating Solid ({}x{})", f.size.width, f.size.height);
    for y in 0..f.size.height {
        for x in 0..f.size.width {
            f.file.write(b"0 255 255 ").unwrap();
        }
        f.file.write("\n".as_bytes()).unwrap();
    }
}

fn vertical_gradient(f: &mut ImageFile) {
    println!(
        "Creating Vertical Gradient ({}x{})",
        f.size.width, f.size.height
    );
    for y in 0..f.size.height {
        for x in 0..f.size.width {
            let (r, g, b) = ((y) % 255, (255 - (y) % 255), 255);
            let color = format!("{} {} {} ", r, g, b);
            f.file.write(color.as_bytes()).unwrap();
        }
        f.file.write("\n".as_bytes()).unwrap();
    }
}

fn horizontal_gradient(f: &mut ImageFile) {
    println!(
        "Creating Horizontal Gradient ({}x{})",
        f.size.width, f.size.height
    );
    for y in 0..f.size.height {
        for x in 0..f.size.width {
            let (r, g, b) = ((x) % 255, (255 - (x) % 255), 255);
            let color = format!("{} {} {} ", r, g, b);
            f.file.write(color.as_bytes()).unwrap();
        }
        f.file.write("\n".as_bytes()).unwrap();
    }
}

fn diagonal_gradient(f: &mut ImageFile) {
    println!("Creating Diagonal ({}x{})", f.size.width, f.size.height);
    for y in 0..f.size.height {
        for x in 0..f.size.width {
            let (r, g, b) = ((x / 2 + y / 2) % 255, (255 - (x / 2 + y / 2) % 255), 255);
            let color = format!("{} {} {} ", r, g, b);
            f.file.write(color.as_bytes()).unwrap();
        }
        f.file.write("\n".as_bytes()).unwrap();
    }
}

fn horizontal_stripes(f: &mut ImageFile) {
    println!(
        "Creating Horizontal Stripes ({}x{})",
        f.size.width, f.size.height
    );
    for y in 0..f.size.height {
        for x in 0..f.size.height {
            let (r, g, b) = (255, 255, 255);

            let color = if y % 2 == 0 {
                format!("{} {} {} ", r, g, b)
            } else {
                format!("{} {} {} ", 255 - r, 255 - g, 255 - b)
            };

            f.file.write(color.as_bytes()).unwrap();
        }
        f.file.write("\n".as_bytes()).unwrap();
    }
}

fn vertical_stripes(f: &mut ImageFile) {
    println!(
        "Creating Vertical Stripes ({}x{})",
        f.size.width, f.size.height
    );
    for y in 0..f.size.height {
        for x in 0..f.size.height {
            let (r, g, b) = (255, 255, 255);

            let color = if x % 2 == 0 {
                format!("{} {} {} ", r, g, b)
            } else {
                format!("{} {} {} ", 255 - r, 255 - g, 255 - b)
            };

            f.file.write(color.as_bytes()).unwrap();
        }
        f.file.write("\n".as_bytes()).unwrap();
    }
}

fn checkerboard(f: &mut ImageFile) {
    println!("Creating Checkerboard ({}x{})", f.size.width, f.size.height);
    for y in 0..f.size.height {
        for x in 0..f.size.height {
            let (r, g, b) = (130, 80, 255);

            let color = if x % 2 == 0 && y % 2 == 0 {
                format!("{} {} {} ", r, g, b)
            } else {
                format!("{} {} {} ", 255 - r, 255 - g, 255 - b)
            };

            f.file.write(color.as_bytes()).unwrap();
        }
        f.file.write("\n".as_bytes()).unwrap();
    }
}

fn main() {
    let size = Size {
        width: 100,
        height: 100,
    };

    std::fs::create_dir_all("img").unwrap();

    solid(&mut create_ppm("img/solid.ppm", size.clone()));
    horizontal_gradient(&mut create_ppm("img/horizontal_gradient.ppm", size.clone()));
    vertical_gradient(&mut create_ppm("img/vertical_gradient.ppm", size.clone()));
    diagonal_gradient(&mut create_ppm("img/diagonal_gradient.ppm", size.clone()));

    horizontal_stripes(&mut create_ppm("img/horizontal_stripes.ppm", size.clone()));
    vertical_stripes(&mut create_ppm("img/vertical_stripes.ppm", size.clone()));
    checkerboard(&mut create_ppm("img/checkerboard.ppm", size.clone()));
}
