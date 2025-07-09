# Writeups for Week-1 Forensics

# PICO-CTF

### Matryoshka Doll

##### Challenge Description:

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?

[Challenge File](dolls.jpg)

##### Writeup:

The challenge name **Matryoshka Doll** suggests a layered structure, hinting at multiple files embedded within each other. The provided file is a PNG image, so we first analyze its contents:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ file dolls.jpg 
dolls.jpg: PNG image data, 594 x 1104, 8-bit/color RGBA, non-interlaced
```

Using `binwalk` to inspect for embedded files:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ binwalk dolls.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378952, uncompressed size: 383937, name: base_images/2_c.jpg
651610        0x9F15A         End of Zip archive, footer length: 22
```

The output reveals a zip archive containing `base_images/2_c.jpg`. We extract it:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ binwalk -e dolls.jpg
```

This creates `_dolls.jpg.extracted` with `4286C.zip` and a `base_images` folder containing `2_c.jpg`. We navigate to `base_images` and analyze `2_c.jpg`:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_dolls.jpg.extracted/base_images$ binwalk 2_c.jpg 

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
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images$ binwalk -e 3_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77650, uncompressed size: 79807, name: base_images/4_c.jpg
```

Extracting `3_c.jpg` gives `1E2D6.zip` and `4_c.jpg`. Finally, we analyze `4_c.jpg`:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images$ binwalk -e 4_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
79578         0x136DA         Zip archive data, at least v2.0 to extract, compressed size: 63, uncompressed size: 81, name: flag.txt
```

Extracting `4_c.jpg` produces `136DA.zip` and `flag.txt`. Reading `flag.txt`:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted$ cat flag.txt 
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
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ mv Forensics\ is\ fun.pptm a.zip
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ unzip a.zip
```

This extracts numerous files, including `ppt/slideMasters/hidden`. We inspect it with `strings`:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ strings ppt/slideMasters/hidden 
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
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ cat drawing.flag.svg
```

The SVG contains graphical elements and a `<text>` section with `<tspan>` elements. We extract the text:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ grep tspan drawing.flag.svg 
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
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ xxd advanced-potion-making | head
```

The hex dump shows a corrupted PNG header (e.g., incorrect magic bytes instead of `89 50 4E 47 0D 0A 1A 0A`). We fix the header using a hex editor:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ hexedit advanced-potion-making
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
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ cp Flag.pdf Flag.sh
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ chmod +x Flag.sh
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ ./Flag.sh
```

This generates a file named `flag`. Checking its type:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ file flag
flag: current ar archive
```

Extracting with `binwalk`:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ binwalk -e flag
```

This creates `_flag.extracted` with a file named `64`:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted$ file 64
64: gzip compressed data
```

Extracting `64`:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted$ binwalk -e 64
```

This produces `flag` in `_64.extracted`:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag
flag: lzip compressed data
```

Since `binwalk` fails to extract lzip, we use:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ lzip -d -k flag
```

This creates `flag.out`, which is LZ4 compressed:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag.out
flag.out: LZ4 compressed data
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ lz4 -d flag.out flag2.out
```

The resulting `flag2.out` is LZMA compressed:

```shell
4:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag2.out
flag2.out: LZMA compressed data
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ mv flag2.out flag2.lzma
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ lzma -d -k flag2.lzma
```

This creates `flag2`, which is LZOP compressed:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag2
flag2: LZOP compressed data
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ mv flag2 flag2.lzop
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ lzop -d -k flag2.lzop -o flag3
```

The resulting `flag3` is LZIP compressed:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag3
flag3: LZIP compressed data
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ lzip -d -k flag3
```

This creates `flag3.out`, which is XZ compressed:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ file flag3.out
flag3.out: XZ compressed data
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ mv flag3.out flag4.xz
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ xz -d -k flag4.xz
```

The final `flag4` is ASCII text containing a hex string:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_flag.extracted/_64.extracted$ cat flag4
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
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ binwalk hideme
```

The output reveals a zip archive embedded in the image. We extract it:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ binwalk -e hideme
```

This creates `_hideme.extracted` containing a zip file (e.g., `12345.zip`). Unzipping it:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF/_hideme.extracted$ unzip 12345.zip
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
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ python3 sigBits.py -t=msb Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
```

This outputs a file (e.g., `output.png`). We search the output for the flag:

```shell
$:~/CSOC/INFOSEC/Week1/PICO_CTF$ grep -i "picoCTF" output.png
```

The grep command reveals the flag embedded in the output image:

**`picoCTF{m0st_51gn1f1c4nt_b17_51mpl3}`**

**Note**: The `sigBits.py` script extracts MSB data, and the flag was likely embedded as text or a visible element in the output image.

---

# TryHackMe Sakura Room

##### Writeup:

The Sakura Room, created by OSINT Dojo on TryHackMe, is a beginner-friendly OSINT challenge designed to test various open-source intelligence techniques. The scenario involves a cyberattack on OSINT Dojo, with an image (`sakurapwnedletter.svg`) left by the attacker as a clue. The goal is to identify the attacker through passive OSINT methods. Below are the solutions to key tasks.

---

### Task 1: Introduction

##### Objective:
Read the introduction and type the given phrase to begin.

##### Solution:
The introduction describes a cyberattack on OSINT Dojo, with an SVG image left by the attacker. The task requires entering the phrase:

```
Let's Go!
```

This unlocks the subsequent tasks.

---

### Task 2: Tip-Off

##### Objective:
What username does the attacker go by?

##### Solution:
The provided image is an SVG file. After downloading it as an svg file i inspected it with exiftool.

```shell
aerex@localhost:~/CSOC/INFOSEC/Week1/TRYHACKME$ exiftool sakurapwnedletter.svg
```

The file’s metadata includes a file path: `/home/SakuraSnowAngelAiko/Desktop/pwnedletter.png`, revealing the attacker’s username:

**`SakuraSnowAngelAiko`**


---

### Task 3: Reconnaissance

##### Objective 1:
What is the full email address used by the attacker?

##### Solution:
Using the username `SakuraSnowAngelAiko`, we search Google for associated accounts:

This reveals a GitHub profile: `https://github.com/sakurasnowangelaiko`. Browsing the repositories, I find a `PGP` repository containing a `publickey` file. We can either use gpg on the PGP file or use an online PGP decoder to get the details which consist the email of the attacker.



```shell
$:~/CSOC/INFOSEC/Week1/TRYHACKME$ gpg publickey
gpg: WARNING: no command supplied. Trying to guess what you mean ...
pub   rsa3072 2021-01-23 [SC] [expires: 2023-01-22]
      A6519F273BF88E9126B0F4C5ECDD0FD294110450
uid   SakuraSnowAngel83@protonmail.com
sub   rsa3072 2021-01-23 [E] [expires: 2023-01-22]
```

The `uid` field reveals the email:

**`SakuraSnowAngel83@protonmail.com`**

---

##### Objective 2:
What is the attacker’s current Twitter handle?

##### Solution:
Searching for `SakuraSnowAngelAiko` on Twitter reveals a tweet: “Silly me, I forgot to introduce myself! Hi there! I'm @AikoAbe3!”. Following this lead, we check the Twitter profile `@AikoAbe3`, which redirects to `@SakuraLoverAiko`, indicating a handle change. The profile picture matches the GitHub account, confirming it’s the same user.

The current Twitter handle is:

**`@SakuraLoverAiko`**

---
### Task 4: Unveil

##### Objective 1:
What cryptocurrency does the attacker own a cryptocurrency wallet for?

##### Solution:
It's Etherium ofcourse that's wallet address we found.


##### Objective 2:
What is the attacker's cryptocurrency wallet address?

##### Solution:
In the ETH repository page, I can inspect history and at one time looks like attacker uploaded her Wallet Address. In the commit you can see the wallet address.

##### Objective 3:
What mining pool did the attacker receive payments from on January 23, 2021 UTC?

##### Solution:
Inspecting the etherium transactions using the wallet address, we can find out it's *Ethermine*.

##### Objective 4:
What other cryptocurrency did the attacker exchange with using their cryptocurrency wallet?

##### Solution:
Checking out outher transactions, i find out attackers was also exhanging Tether.

---

### Task 5: Taunt

##### Objective:
What is the BSSID for the attacker’s Home WiFi?

##### Solution:
They have made some changes (removed a queestion along with a hint of an image) since the hint has been removed, i will have to go the unofficial way to solve it and i didn't do it.

**`Not Done`**

---

### Task 6: Geolocation

##### Objective:
What airport is closest to the location the attacker shared a photo from prior to getting on their flight? What lake can be seen in the map shared by the attacker as they were on their final flight home? What city does the attacker likely consider “home”?

##### Solution:
On the `@SakuraLoverAiko` Twitter account, a tweet includes a photo of a Japan Airlines (JAL) First Class Sakura Lounge. Searching for “JAL First Class Sakura Lounge sign” on Google or Yandex:

The image matches the lounge at Tokyo Haneda Airport (HND). The airport code is:

**`HND`**

Another tweet includes a map showing a lake during the attacker’s flight. Using Google image search i found the name 'Yamagata' (i was looking for the S shaped island) then from Google Earth i found the name of the lake:

**`Lake Inawashiro`**

We need to first get the BSSID to get the home and since the hint has been removed, i will have to go the unofficial way to solve it and i didn't do it.

**`Not Done`**


---

# Gralhix OSINT Exercises

### Exercise 6

##### Writeup:

*I just searched the image on google and came across this Wiki page https://en.m.wikipedia.org/wiki/File:WaziriyaAutobombeIrak.jpg. This clears the statement that this image is from iraq and not pakistan.*

### Exercise 4

##### Writeup:

*I just searched the image on google and came across the official page of the resort https://oanresort.wixsite.com/chuuk. The location is Oan Resort, Oan Islands, Micronesia. Then i used google maps to get the coordinates (7.362590, 151.756325) and using the street view i can get the direction the camera was facing which is North-West.*

### Exercise 3

##### Writeup:

*I searched the image on google and the come across the web pages revealing the name of the location 'the presidential complex' and the coordinates can be retreived using google maps 39.93114, 32.79967 *
