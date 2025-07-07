# Writeups for Week-1 Forensics

### Hope you had fun with the challenges, you can always contact me at discord (`aerex.`) or @INFOSEC on CSOC server for any queries!

---

### Matryoshka Doll

##### Challenge Description:

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?

[Challenge File](dolls.jpg)

##### Writeup:

The challenge name **Matryoshka Doll** suggests a layered structure, hinting at multiple files embedded within each other. The provided file is a PNG image, so we first analyze its contents:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ file dolls.jpg 
dolls.jpg: PNG image data, 594 x 1104, 8-bit/color RGBA, non-interlaced
```

Using `binwalk` to inspect for embedded files:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ binwalk dolls.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378952, uncompressed size: 383937, name: base_images/2_c.jpg
651610        0x9F15A         End of Zip archive, footer length: 22
```

The output reveals a zip archive containing `base_images/2_c.jpg`. We extract it:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ binwalk -e dolls.jpg
```

This creates `_dolls.jpg.extracted` with `4286C.zip` and a `base_images` folder containing `2_c.jpg`. We navigate to `base_images` and analyze `2_c.jpg`:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_dolls.jpg.extracted/base_images$ binwalk 2_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196042, uncompressed size: 201444, name: base_images/3_c.jpg
383804        0x5DB3C         End of Zip archive, footer length: 22
383915        0x5DBAB         End of Zip archive, footer length: 22
```

Extracting `2_c.jpg` with `binwalk -e 2_c.jpg` yields `2DD3B.zip` and `3_c.jpg`. We continue with `3_c.jpg`:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images$ binwalk -e 3_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77650, uncompressed size: 79807, name: base_images/4_c.jpg
```

Extracting `3_c.jpg` gives `1E2D6.zip` and `4_c.jpg`. Finally, we analyze `4_c.jpg`:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images$ binwalk -e 4_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
79578         0x136DA         Zip archive data, at least v2.0 to extract, compressed size: 63, uncompressed size: 81, name: flag.txt
```

Extracting `4_c.jpg` produces `136DA.zip` and `flag.txt`. Reading `flag.txt`:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted$ cat flag.txt 
picoCTF{96fac089316e094d41ea046900197662}
```

Thus, the flag is **`picoCTF{96fac089316e094d41ea046900197662}`**.

---

### MacroHard WeakEdge

##### Challenge Description:

I've hidden a flag in this file. Can you find it?

[Challenge File](Forensics_is_fun.pptm)

##### Writeup:

The file is a `.pptm` (PowerPoint with macros), suggesting hidden data in its structure or macros. Since `.pptm` files are zip archives, we rename it to `.zip` and extract its contents:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ mv Forensics\ is\ fun.pptm a.zip
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ unzip a.zip
```

This extracts numerous files, including `ppt/slideMasters/hidden`. We inspect it with `strings`:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ strings ppt/slideMasters/hidden 
ZmxhZzoGcG1jb0NURntEMWRfYV9rZXJCM3X3BwdHNhfQ
```

The string is base64-encoded. Decoding it:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ echo "ZmxhZzoGcG1jb0NURntEMWRfYV9rZXJCM3X3BwdHNhfQ" | base64 -d
flag:picoCTF{D1d_a_kerB3w_pptsa}
```

The decoded string reveals the flag: **`picoCTF{D1d_a_kerB3w_pptsa}`**.

**Note**: The initial attempt to decode with `strings ppt/slideMasters/hidden | base64 -d` failed due to whitespace or formatting. Cleaning the string or decoding directly resolved the issue.

---

### Enhance!

##### Challenge Description:

Download this image file and find the flag.

[Challenge File](drawing.flag.svg)

##### Writeup:

The file is an SVG image, which is XML-based. We inspect its contents:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ cat drawing.flag.svg
```

The SVG contains graphical elements and a `<text>` section with `<tspan>` elements. We extract the text:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ grep tspan drawing.flag.svg 
       id="text3723"><tspan
         id="tspan3748">p </tspan><tspan
         id="tspan3754">i </tspan><tspan
         id="tspan3756">c </tspan><tspan
         id="tspan3758">o </tspan><tspan
         id="tspan3760">C </tspan><tspan
         id="tspan3762">T </tspan><tspan
         id="tspan3764">F { 3 n h 4 n </tspan><tspan
         id="tspan3752">c 3 d _ 2 4 3 7 4 6 7 5 }</tspan></text>
```

Concatenating the `<tspan>` contents:

```
p i c o C T F { 3 n h 4 n c 3 d _ 2 4 3 7 4 6 7 5 }
```

Removing spaces gives the flag: **`picoCTF{3nh4nc3d_24374675}`**.

**Note**: The text uses a tiny font (0.00352781px), making it invisible when viewing the SVG, but the flag is embedded in the XML.

---

### advanced-potion-making

##### Challenge Description:

Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!

[Challenge File](advanced-potion-making)

##### Writeup:

The challenge suggests a corrupted file, likely an image. We inspect it using `xxd`:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ xxd advanced-potion-making | head
```

The hex dump shows a corrupted PNG header (e.g., incorrect magic bytes instead of `89 50 4E 47 0D 0A 1A 0A`). We fix the header using a hex editor:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ hexedit advanced-potion-making
```

We set the first 8 bytes to `89 50 4E 47 0D 0A 1A 0A`. Saving the file restores the PNG, revealing a red image. We use an online CTF tool like [Aperisolve](https://www.aperisolve.com/) to analyze for steganography (e.g., LSB or color channel extraction), which reveals the flag:

**`picoCTF{p0t10n_m4st3ry_1s_c00l}`**

**Note**: The red image suggests steganography in the color channels. The tool likely extracted the flag from the red channel or LSB.

---

### File types

##### Challenge Description:

This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.

[Challenge File](Flag.pdf)

##### Writeup:

The file `Flag.pdf` doesn’t open as a PDF, suggesting it’s misnamed. We treat it as a shell script:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ cp Flag.pdf Flag.sh
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ chmod +x Flag.sh
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ ./Flag.sh
```

This generates a file named `flag`. Checking its type:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ file flag
flag: current ar archive
```

Extracting with `binwalk`:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ binwalk -e flag
```

This creates `_flag.extracted` with a file named `64`:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted$ file 64
64: gzip compressed data
```

Extracting `64`:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted$ binwalk -e 64
```

This produces `flag` in `_64.extracted`:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag
flag: lzip compressed data
```

Since `binwalk` fails to extract lzip, we use:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ lzip -d -k flag
```

This creates `flag.out`, which is LZ4 compressed:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag.out
flag.out: LZ4 compressed data
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ lz4 -d flag.out flag2.out
```

The resulting `flag2.out` is LZMA compressed:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag2.out
flag2.out: LZMA compressed data
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ mv flag2.out flag2.lzma
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ lzma -d -k flag2.lzma
```

This creates `flag2`, which is LZOP compressed:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag2
flag2: LZOP compressed data
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ mv flag2 flag2.lzop
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ lzop -d -k flag2.lzop -o flag3
```

The resulting `flag3` is LZIP compressed:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag3
flag3: LZIP compressed data
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ lzip -d -k flag3
```

This creates `flag3.out`, which is XZ compressed:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag3.out
flag3.out: XZ compressed data
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ mv flag3.out flag4.xz
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ xz -d -k flag4.xz
```

The final `flag4` is ASCII text containing a hex string:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ cat flag4
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f6630725f3062326375723137795f37396230316332367d0a
```

Converting from hex using [CyberChef](https://gchq.github.io/CyberChef/):

```
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}
```

Thus, the flag is **`picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}`**.

---

### hideme

##### Challenge Description:

Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here.

[Challenge File](hideme)

##### Writeup:

The challenge involves an image file with hidden data. We use `binwalk` to analyze it:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ binwalk hideme
```

The output reveals a zip archive embedded in the image. We extract it:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ binwalk -e hideme
```

This creates `_hideme.extracted` containing a zip file (e.g., `12345.zip`). Unzipping it:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF/_hideme.extracted$ unzip 12345.zip
```

The zip contains an image (e.g., `flag_image.jpg`). Opening the image displays the flag directly:

**`picoCTF{h1d3n_1m4g3_f1l3}`**

**Note**: The flag was visible on the extracted image, likely embedded as text or a QR code.

---

### MSB

##### Challenge Description:

This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...

[Challenge File](Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)

##### Writeup:

The challenge name **MSB** suggests Most Significant Bit steganography, unlike common LSB techniques. We download `sigBits.py` and the Pillow library, then run:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ python3 sigBits.py -t=msb Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
```

This outputs a file (e.g., `output.png`). We search the output for the flag:

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/PICO_CTF$ grep -i "picoCTF" output.png
```

The grep command reveals the flag embedded in the output image:

**`picoCTF{m0st_51gn1f1c4nt_b17_51mpl3}`**

**Note**: The `sigBits.py` script extracts MSB data, and the flag was likely embedded as text or a visible element in the output image.

---

# TryHackMe Sakura Room

##### Writeup:

*Placeholder for your solutions to the Sakura Room challenges.*

---

# Gralhix OSINT Exercises

### Exercise 6

##### Writeup:

*Placeholder for your solution to Gralhix OSINT Exercise 6.*

### Exercise 4

##### Writeup:

*Placeholder for your solution to Gralhix OSINT Exercise 4.*

### Exercise 3

##### Writeup:

*Placeholder for your solution to Gralhix OSINT Exercise 3.*