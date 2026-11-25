#!/usr/bin/env python3
"""Draw 'The World' front page for Tuesday, 25 November 2026.

Every headline below traces to a news report verified for 24-25 Nov 2026
(see stories.md in the work dir for outlet and headline per story).
The drawing is done entirely with Pillow: no network, no photos, no
external assets. Type is DejaVu (system fonts), black on off-white,
laid out as a classic three-column broadsheet front page.
"""
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (253, 253, 248)
INK = (12, 12, 12)
GREY = (70, 70, 70)
RULE = (30, 30, 30)
ACCENT = (140, 20, 20)
BAR = (18, 18, 18)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def font(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


F_MAST = font("DejaVuSerif-Bold.ttf", 64)
F_DATE = font("DejaVuSans-Bold.ttf", 18)
F_META = font("DejaVuSans.ttf", 11)
F_KICK = font("DejaVuSans-Bold.ttf", 12)
F_LEAD = font("DejaVuSerif-Bold.ttf", 29)
F_LEAD_DECK = font("DejaVuSerif.ttf", 14)
F_SECT = font("DejaVuSans-Bold.ttf", 12)
F_HEAD = font("DejaVuSerif-Bold.ttf", 13)
F_DEK = font("DejaVuSans.ttf", 11)

MARGIN = 22
COL_W = 320
GUTTER = 12
COL_X = [MARGIN, MARGIN + COL_W + GUTTER, MARGIN + 2 * (COL_W + GUTTER)]


def wrap(draw, text, fnt, width):
    """Wrap text to the given pixel width, word by word."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_item(draw, x, y, headline, dek, width):
    """One dense item: bold headline (max 2 lines) + one-line standfirst."""
    head_lines = wrap(draw, headline, F_HEAD, width)
    assert len(head_lines) <= 2, f"headline too long: {headline!r} -> {head_lines}"
    for line in head_lines:
        draw.text((x, y), line, font=F_HEAD, fill=INK)
        y += 17
    assert draw.textlength(dek, font=F_DEK) <= width, f"dek too long: {dek!r}"
    draw.text((x, y), dek, font=F_DEK, fill=GREY)
    y += 16
    draw.line([(x, y + 2), (x + width, y + 2)], fill=(190, 190, 185), width=1)
    return y + 10


def draw_section_head(draw, x, y, label, width):
    draw.rectangle([x, y, x + width, y + 18], fill=BAR)
    draw.text((x + 7, y + 3), label, font=F_SECT, fill=(255, 255, 255))
    return y + 25


def draw_continued(draw, x, y, label, width):
    draw.text((x, y), label + "  -  CONTINUED", font=F_SECT, fill=GREY)
    draw.line([(x, y + 16), (x + width, y + 16)], fill=(150, 150, 145), width=1)
    return y + 23


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    draw.line([(MARGIN, 12), (W - MARGIN, 12)], fill=RULE, width=3)
    title = "The World"
    tw = draw.textlength(title, font=F_MAST)
    draw.text(((W - tw) / 2, 16), title, font=F_MAST, fill=INK)
    date_line = "Tuesday, 25 November 2026"
    dw = draw.textlength(date_line, font=F_DATE)
    draw.text(((W - dw) / 2, 86), date_line, font=F_DATE, fill=ACCENT)
    draw.text((MARGIN, 88), "Vol. CXII  \u00b7  No. 329", font=F_META, fill=GREY)
    right_meta = "World News  \u00b7  46 Stories"
    draw.text((W - MARGIN - draw.textlength(right_meta, font=F_META), 88),
              right_meta, font=F_META, fill=GREY)
    draw.line([(MARGIN, 110), (W - MARGIN, 110)], fill=RULE, width=2)
    draw.line([(MARGIN, 114), (W - MARGIN, 114)], fill=RULE, width=1)

    # ---- Lead story -----------------------------------------------------
    y = 122
    draw.text((MARGIN, y), "LEAD STORY  \u00b7  TECHNOLOGY  \u00b7  MARKETS",
              font=F_KICK, fill=ACCENT)
    y += 18
    lead_head = "Nvidia rally fades as Trump role probed"
    for line in wrap(draw, lead_head, F_LEAD, W - 2 * MARGIN):
        draw.text((MARGIN, y), line, font=F_LEAD, fill=INK)
        y += 33
    deck = "Shares fall; Huang admits conduct breach, pardon floated."
    for line in wrap(draw, deck, F_LEAD_DECK, W - 2 * MARGIN):
        draw.text((MARGIN, y), line, font=F_LEAD_DECK, fill=GREY)
        y += 18
    y += 2
    draw.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=2)
    body_top = y + 8

    # ---- Sections: (label, [(headline, standfirst), ...]) ---------------
    sections = [
        ("NORTH AMERICA", [
            ("Abrego Garcia leaves US for Spain",
             "Mistaken deportation saga ends in voluntary exit."),
            ("Six die in Gulf plane crash",
             "Cessna bound for Florida; two boys among six aboard."),
            ("CIA open-source system breached",
             "Unclassified network hit; no classified data involved."),
            ("Fort Hood shooter seeks execution stay",
             "Hasan asks court to delay firing-squad execution."),
            ("Shein pays $100m in FTC settlement",
             "Misleading shipping, review and cotton claims alleged."),
            ("Army to detonate Iowa explosives",
             "Relocation urged for Wednesday lead-azide blast."),
            ("Trump pardons Freedom and Feathers",
             "Thanksgiving turkeys spared at White House ceremony."),
            ("Carney roasts Trump with impersonator",
             "Canada PM enlists comedians at press-gallery dinner."),
        ]),
        ("LATIN AMERICA", [
            ("Cartagena hostages freed in raid",
             "All freed after siege; one captor killed, police say."),
            ("Car bomb wounds 23 in Villavicencio",
             "Blast outside Meta governor's offices; no deaths reported."),
            ("Venezuela reveals $237.5bn debt pile",
             "First full framework in years; restructuring eyed."),
            ("Mexico to try El Chapo Isidro at home",
             "Attorney general resists US extradition request for now."),
            ("WHO chief urges end to Cuba fuel blockade",
             "Tedros cites shortages, surgery backlog in Havana."),
            ("Polish president meets Milei in Buenos Aires",
             "First Polish presidential visit to Argentina in 31 years."),
        ]),
        ("EUROPE", [
            ("Sarkozy and Bruni ordered to trial",
             "Corruption case over witness-retraction plot proceeds."),
            ("Spain split ahead of snap election",
             "Far right could enter government for first time."),
            ("Russian war deaths near 500,000",
             "BBC/Mediazona analysis puts toll at 490,334."),
            ("Drones hit Samara refineries; Putin vows reply",
             "Fires at oil sites; Putin says retaliation inevitable."),
            ("Sweden sets Kristersson PM vote",
             "Vote on 30 Nov after 72 days without a government."),
            ("UK energy bills to soar 26% from January",
             "Ofgem cap hits highest in almost four years."),
            ("Hera returns to asteroid crash scene",
             "ESA craft to study Dimorphos after 2022 DART hit."),
        ]),
        ("AFRICA", [
            ("Senegal regain Africa Cup title",
             "CAS overturns ruling that gave trophy to Morocco."),
            ("Congo plane missing; rebels claim shoot-down",
             "Army cites weather; rebel claim unverified."),
            ("Nollywood legend Pete Edochie dies at 79",
             "Actor dies in Enugu after prostate illness, family says."),
            ("Amnesty urges Tigray shelling probe",
             "14 civilians verified killed in Alamata strikes."),
            ("Cameroon conflict scars its children",
             "BBC hears victims of a decade of fighting."),
            ("Nigerian monarch, 92, suspended",
             "Traditional ruler suspended amid assault claims."),
        ]),
        ("MIDDLE EAST", [
            ("Houthis hit Riyadh tower; 11 wounded",
             "Second strike on tallest tower in less than a week."),
            ("Gaza strike kills Hamas security chief",
             "Seven killed in strikes despite ceasefire, medics say."),
            ("Iran claims tankers hit Hormuz mines",
             "IRGC says two tankers caught fire; claim unverified."),
            ("Iran flogs singer over unveiled concert",
             "Parastoo Ahmadi, four colleagues lashed in Qom."),
            ("Coalition orders Hodeidah port cleared",
             "Warning as Houthis threaten Red Sea ports."),
            ("Katz warns Iran seeks chemical arms",
             "Israel will stop Tehran acquiring them, minister says."),
        ]),
        ("ASIA-PACIFIC", [
            ("Shenzhou-24 lifts off with Pakistani astronaut",
             "First foreigner aboard China's Tiangong station."),
            ("China probes Shanghai party chief",
             "Chen Jining is 4th Politburo member probed since 2025."),
            ("Bangladesh garment wage up 36%",
             "Minimum rises to Tk17,000; fresh protests follow."),
            ("Dozens feared trapped in Indonesian mine",
             "Floods inundate illegal gold mine shaft in West Java."),
            ("Myanmar tops world landmine toll again",
             "1,891 casualties in 2025, Landmine Monitor says."),
            ("Huawei convicted on 10 US counts",
             "Guilty on fraud, secrets theft; cleared of racketeering."),
            ("Hong Kong marks year since Tai Po fire",
             "Survivors mourn 168 dead; accountability questioned."),
        ]),
        ("OCEANIA", [
            ("Australia, Solomons sign security treaty",
             "Canberra named primary partner; no foreign bases."),
            ("Ex-policeman guilty of Sydney double murder",
             "Jury convicts Beau Lamarre over 2024 killings."),
            ("Fiji drought emergency may run into 2027",
             "Water shortages expected into early 2027."),
            ("Brookfield bid lifts Reliance Worldwide",
             "Shares hit 20-month high on pension-fund backing."),
            ("El Nino raises Guam drought risk",
             "Guam, Northern Marianas face dry start to 2027."),
        ]),
    ]

    # Balance the three columns at 15 items each, keeping section
    # order and never splitting a section heading from its first item.
    columns = [[], [], []]  # lists of ("head", label) / ("cont", label) / ("item", h, d)
    col_counts = [0, 0, 0]
    col = 0
    # Column capacities: 15 items each for this edition's wrap lengths.
    capacities = [15, 15, 99]
    for label, items in sections:
        for i, (h, d) in enumerate(items):
            if col_counts[col] >= capacities[col] and col < 2:
                col += 1
            if i == 0:
                columns[col].append(("head", label))
            elif col_counts[col] == 0:
                columns[col].append(("cont", label))
            columns[col].append(("item", h, d))
            col_counts[col] += 1

    footer_y = H - 26
    for x, entries in zip(COL_X, columns):
        y = body_top
        for entry in entries:
            if entry[0] == "head":
                y = draw_section_head(draw, x, y, entry[1], COL_W)
            elif entry[0] == "cont":
                y = draw_continued(draw, x, y, entry[1], COL_W)
            else:
                y = draw_item(draw, x, y, entry[1], entry[2], COL_W)
            assert y <= footer_y - 4, f"column overflow at {entry}"
        draw.line([(x, body_top - 4), (x, y)], fill=(200, 200, 195), width=1)

    # ---- Footer ---------------------------------------------------------
    draw.line([(MARGIN, footer_y - 6), (W - MARGIN, footer_y - 6)],
              fill=RULE, width=1)
    foot = "The World  \u00b7  Tuesday, 25 November 2026  \u00b7  All stories from reports published 24-25 November 2026"
    fw = draw.textlength(foot, font=F_META)
    draw.text(((W - fw) / 2, footer_y + 2), foot, font=F_META, fill=GREY)

    out = Path(__file__).with_name("entry.png")
    img.save(out, optimize=True)
    print(f"wrote {out} {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
