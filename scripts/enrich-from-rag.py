#!/usr/bin/env python3
"""
Enrich timeline-data.json with content from RAG corpus.
Uses extracted text from dr-cortes-rag-corpus to enhance:
- Biography with personal background
- Decade summaries
- Work descriptions
"""

import json
from pathlib import Path

# Paths
WEBSITE_DIR = Path(__file__).parent.parent
RAG_CORPUS_DIR = Path(__file__).parent.parent.parent / "dr-cortes-rag-corpus"
TIMELINE_PATH = WEBSITE_DIR / "assets" / "data" / "timeline-data.json"
OUTPUT_PATH = WEBSITE_DIR / "assets" / "data" / "timeline-data.json"

def load_timeline():
    """Load existing timeline data."""
    with open(TIMELINE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_enhanced_biography():
    """Create enhanced biography from RAG corpus."""
    return {
        "name": "Dr. Carlos E. Cortés",
        "title": "Edward A. Dickson Emeritus Professor of History",
        "institution": "University of California, Riverside",
        "birthYear": 1934,
        "careerStart": 1968,
        "totalWorks": "400+",

        # Enhanced bio from RAG corpus
        "bio": "Dr. Carlos E. Cortés is a pioneering figure in multicultural education, ethnic studies, and diversity scholarship with a career spanning over five decades. Born in 1934 in Kansas City, Missouri, he grew up navigating the intersection of cultures as the son of Carlos Cortés, a Mexican Catholic immigrant from Guadalajara, and Florence Hoffman, the Jewish American daughter of Ukrainian and Austrian immigrants. This unique upbringing in a racially segregated, religiously divided community profoundly shaped his life's work on diversity and inclusion.",

        # NEW: Personal background story
        "personal_background": "In 1933, Carlos Cortés's father, a Mexican Catholic immigrant from Guadalajara, married Florence Hoffman, a Jewish American woman—an intermarriage before its time. Growing up in post-WWII Kansas City, young Carlos learned to navigate multiple identities. A defining moment came in 1949 when, as a sophomore, he was pressured by a Spanish teacher to go by 'Carl' instead of Carlos. His father stormed to the principal's office declaring: 'My son's name is Carlos. His father's name is Carlos. His grandfather's name was Carlos. His great-grandfather's name was Carlos. And I'll be damned if you're going to call him anything but Carlos.' This became a touchstone for authentic inclusivity throughout his career. He later wrote about these experiences in his memoir 'Rose Hill: An Intermarriage before Its Time' (2012) and adapted it into a one-person play performed nationwide.",

        # NEW: Career timeline highlights
        "timeline_highlights": [
            {"year": 1934, "event": "Born in Kansas City, Missouri to a Mexican Catholic father and Jewish American mother"},
            {"year": 1962, "event": "Began graduate study in history and literature at University of New Mexico"},
            {"year": 1968, "event": "Joined UC Riverside faculty in January; began 57-year career in academia"},
            {"year": 1970, "event": "Taught UCR's first Chicano History class; drafted first diversity graduation requirement"},
            {"year": 1971, "event": "Served on California's first statewide textbook evaluation task force for ethnic content"},
            {"year": 1973, "event": "Contributed 'Chicanos' chapter to James Banks' 'Teaching Ethnic Studies,' launching national speaking career"},
            {"year": 1974, "event": "Published 'Gaúcho Politics in Brazil,' winning the Hubert Herring Memorial Award"},
            {"year": 2000, "event": "Published 'The Children Are Watching'; joined Dora the Explorer as Creative/Cultural Advisor"},
            {"year": 2009, "event": "Received NAACP Image Award for work with Nickelodeon"},
            {"year": 2016, "event": "City of Riverside establishes Carlos E. Cortés Diversity and Inclusion Award"},
            {"year": 2020, "event": "First UCR faculty to receive Constantine Panunzio Distinguished Emeriti Award"},
            {"year": 2021, "event": "Eight principles he authored adapted into California's Ethnic Studies Model Curriculum"},
            {"year": 2022, "event": "Became Consulting Humanist for The Cheech Marin Museum of Chicano Art & Culture"},
            {"year": 2024, "event": "Celebrated 90th birthday; began donating professional papers to UCR Special Collections"}
        ],

        # Existing awards
        "awards": [
            {
                "year": 1974,
                "award": "Hubert Herring Memorial Award",
                "description": "Pacific Coast Council on Latin American Studies for Gaúcho Politics in Brazil"
            },
            {
                "year": 2009,
                "award": "NAACP Image Award",
                "description": "Creative/Cultural Advisory work for Nickelodeon"
            },
            {
                "year": 2017,
                "award": "Honorable Mention - International Latino Book Awards",
                "description": "Best Book of Poetry for Fourth Quarter: Reflections of a Cranky Old Man"
            },
            {
                "year": 2020,
                "award": "Constantine Panunzio Distinguished Emeriti Award",
                "description": "University of California (first faculty member from UCR to receive this honor)"
            }
        ]
    }

def create_decade_summaries():
    """Create enhanced decade summaries from RAG corpus."""
    return {
        "1970s": {
            "summary": "The 1970s marked Dr. Cortés's emergence as a pioneer in Chicano studies and multicultural education. In January 1970, he taught UCR's first Chicano History class and drafted the university's first diversity graduation requirement—a precursor to requirements now at one-third of U.S. colleges. His 1971 service on California's first statewide textbook evaluation task force for ethnic content launched his national speaking career. His chapter 'Chicanos' in James Banks' influential 1973 book 'Teaching Ethnic Studies' was widely adopted for teacher training, establishing him as a founding voice in K-12 multicultural education. As he later reflected: 'We championed bridge-building inclusion without dividing the world into the oppressed and their oppressors. We committed ourselves to critical, uninhibited dialogue. When we sang \"We Shall Overcome,\" we meant it.'",
            "key_achievements": [
                "Taught UCR's first Chicano History class (1970)",
                "Drafted UCR's first diversity graduation requirement",
                "Served on California's first ethnic content textbook task force (1971)",
                "Published 'Chicanos' chapter in James Banks' seminal multicultural education text",
                "Won Hubert Herring Memorial Award for 'Gaúcho Politics in Brazil' (1974)"
            ]
        },
        "1980s": {
            "summary": "The 1980s saw Dr. Cortés become a nationally recognized leader in multicultural education and bilingual education scholarship. His work on language minority students and Hispanic experiences in the United States helped shape educational policy. He conducted diversity training across 48 states (missing only Delaware and West Virginia), working with 'both liberals and conservatives, Republicans and Democrats, often in states that today ban wokeness.' This decade established his reputation as a bridge-builder who could engage audiences across the political spectrum.",
            "key_achievements": [
                "Published 'Beyond Language: Social and Cultural Factors in Schooling Language Minority Students'",
                "Edited 'Hispanics in the United States' book series",
                "Established national reputation as diversity trainer across 48 states",
                "Built bridges across political divides on diversity issues"
            ]
        },
        "1990s": {
            "summary": "During the 1990s, Dr. Cortés expanded his focus to media literacy and how mass media teach about diversity. His educational videos on classroom diversity became widely used in teacher training programs nationwide. This period laid the groundwork for his groundbreaking work on media representation that would culminate in his 2000 book 'The Children Are Watching.'",
            "key_achievements": [
                "Produced 'Video Journal of Education: Diversity in the Classroom'",
                "Expanded research on media and diversity education",
                "Continued national speaking and consulting on multicultural education"
            ]
        },
        "2000s": {
            "summary": "The 2000s brought Dr. Cortés's most visible cultural impact. His 2000 book 'The Children Are Watching: How the Media Teach about Diversity' became influential in the field. That same year, he joined Nickelodeon's 'Dora the Explorer' as Creative/Cultural Advisor, a role he held for over 20 years. He championed making Dora 'pan-Latino'—a proud Latina with no specific national origin, allowing Latino children of all backgrounds to identify with her. As he explained: 'Dora constantly draws on her bilingual skills to build intercultural bridges.' His work earned an NAACP Image Award in 2009.",
            "key_achievements": [
                "Published 'The Children Are Watching: How the Media Teach about Diversity'",
                "Became Creative/Cultural Advisor for 'Dora the Explorer' (2000-2020s)",
                "Authored 'The Making—and Remaking—of a Multiculturalist' autobiography",
                "Drafted 'Building a More Inclusive Riverside Community' statement",
                "Received NAACP Image Award (2009)"
            ]
        },
        "2010s": {
            "summary": "The 2010s showcased Dr. Cortés's range as both scholar and creative writer. His 2012 memoir 'Rose Hill: An Intermarriage before Its Time' explored growing up at the intersection of Mexican Catholic and Jewish American identities. His poetry collection 'Fourth Quarter' won honors at the International Latino Book Awards. He continued scholarly work with the 'Multicultural America Encyclopedia' and research on free speech and diversity through a UC fellowship. The City of Riverside honored his legacy by establishing the Carlos E. Cortés Diversity and Inclusion Award in 2016.",
            "key_achievements": [
                "Published memoir 'Rose Hill: An Intermarriage before Its Time' (2012)",
                "Edited 'Multicultural America: A Multimedia Encyclopedia'",
                "Received International Latino Book Awards honorable mention for poetry",
                "City of Riverside establishes award in his name (2016)",
                "UC National Center fellowship on free speech and civic engagement (2019)"
            ]
        },
        "2020s": {
            "summary": "Now in his 90s, Dr. Cortés remains remarkably active. He authored eight principles that were adapted into California's groundbreaking Ethnic Studies Model Curriculum (2021). He became Consulting Humanist for The Cheech Marin Museum of Chicano Art & Culture, conducting filmed conversations exploring Chicano art and culture. In 2020, he became the first UCR faculty member to receive the Constantine Panunzio Distinguished Emeriti Award. His 'Renewing Diversity' blog series advocates for returning to the bridge-building, optimistic spirit of 1970s multicultural education. At 90, he continues to write, speak, and challenge the field: 'We can still overcome.'",
            "key_achievements": [
                "Authored 8 principles adapted into California's Ethnic Studies Model Curriculum",
                "First UCR faculty to receive Constantine Panunzio Distinguished Emeriti Award",
                "Became Consulting Humanist for The Cheech museum (2022)",
                "Cultural consultant on 'Puss in Boots: The Last Wish' (2022)",
                "Began donating professional papers to UCR Special Collections (2024)",
                "Active blogger with 'Renewing Diversity' series"
            ]
        }
    }

def enhance_work_descriptions():
    """Create enhanced descriptions for key works."""
    return {
        # Key to match: lowercase title contains this string
        "chicano history": {
            "enhanced_description": "Dr. Cortés's pioneering Chicano History course at UCR, launched in January 1970, was among the first of its kind at a major university. The course featured innovative pedagogical approaches, including a family history research paper that evolved to be more inclusive after a non-Chicano student's request. As Cortés later reflected: 'If you want to be inclusive, you can't exclude.' This course helped establish Chicano Studies as a legitimate academic field.",
            "related_themes": ["ethnic studies", "curriculum innovation", "inclusive pedagogy"]
        },
        "gaucho politics": {
            "enhanced_description": "Based on his doctoral dissertation, this scholarly monograph examined regional Brazilian politics from 1930-1964. It won the Hubert Herring Memorial Award from the Pacific Coast Council on Latin American Studies, establishing Cortés's reputation as a serious Latin American historian before his transition to multicultural education scholarship.",
            "related_themes": ["Latin American history", "Brazilian politics", "doctoral research"]
        },
        "children are watching": {
            "enhanced_description": "Published in 2000, this influential book analyzes how mass media—television, film, news, advertising—teach viewers about diversity, often without viewers realizing they are being educated. The book's publication coincided with Cortés joining Nickelodeon's 'Dora the Explorer' as Creative/Cultural Advisor, allowing him to put his media literacy theories into practice on one of children's television's most successful shows.",
            "related_themes": ["media literacy", "diversity in media", "informal education"]
        },
        "dora the explorer": {
            "enhanced_description": "For over two decades, Dr. Cortés served as Creative/Cultural Advisor for Nickelodeon's groundbreaking show. He advocated for making Dora 'pan-Latino'—a proud Latina without a specific national origin—so children of all Latino backgrounds could identify with her. As he explained: 'Dora constantly draws on her bilingual skills to build intercultural bridges.' His work earned an NAACP Image Award in 2009. The show demonstrated how children's media can model inclusive, additive diversity.",
            "related_themes": ["children's media", "Latino representation", "bilingual education", "cultural consulting"]
        },
        "rose hill": {
            "enhanced_description": "This memoir explores Cortés's unique upbringing as the son of a Mexican Catholic immigrant father from Guadalajara and a Jewish American mother of Ukrainian and Austrian heritage. Set in racially segregated post-WWII Kansas City, it chronicles how navigating multiple identities shaped his life's work on diversity. The book includes the now-famous 'Carl moment' when his father defended his right to his Mexican name. Cortés later adapted the memoir into a one-person play performed across the United States.",
            "related_themes": ["memoir", "intermarriage", "identity", "Kansas City", "Jewish-Mexican heritage"]
        },
        "ethnic studies": {
            "enhanced_description": "Dr. Cortés authored eight basic curriculum principles for high school Ethnic Studies that were adapted into outcomes on pages 16-20 of California's final Model Curriculum, adopted in March 2021. This work contributed to AB 101, making California the first state to require ethnic studies for high school graduation. His principles drew on five decades of multicultural education experience and his 1970s work on the state's first textbook evaluation task force.",
            "related_themes": ["curriculum development", "California education policy", "high school requirements"]
        },
        "anti-racism vision": {
            "enhanced_description": "In 2020, Dr. Cortés authored a two-page anti-racism vision statement for the City of Riverside, which was adopted 6-1 by the City Council on October 20, 2020. This built on his earlier work drafting 'Building a More Inclusive Riverside Community' (2001) for Mayor Ronald Loveridge's Multicultural Forum, which established inclusivity as a basic city principle.",
            "related_themes": ["civic engagement", "anti-racism", "local government", "Riverside"]
        },
        "cheech": {
            "enhanced_description": "As Consulting Humanist for The Cheech Marin Museum of Chicano Art & Culture (opened June 2022 in Riverside), Dr. Cortés conducts filmed 'Conversations at The Cheech' exploring Chicano art and culture. His vision aligns with founder Cheech Marin's: making Chicano art everybody's art through 'mutual respect, mutual enrichment, and mutual identification'—a capacious we-ness that expands rather than excludes.",
            "related_themes": ["Chicano art", "museum consulting", "cultural institutions", "Riverside"]
        },
        "renewing multicultural": {
            "enhanced_description": "Based on his 2024 NAME conference keynote in Anaheim, this article advocates for returning to the founding principles of 1970s multicultural education: bridge-building inclusion, uninhibited dialogue, and optimistic vision. Cortés identifies 'three bad habits' in contemporary diversity work and calls for course correction: 'We can still overcome.'",
            "related_themes": ["multicultural education renewal", "diversity critique", "bridge-building"]
        }
    }

def apply_enhancements(timeline, decade_summaries, work_enhancements):
    """Apply enhancements to timeline data."""

    # Enhance decades with summaries
    for decade_key, summary_data in decade_summaries.items():
        if decade_key in timeline["decades"]:
            timeline["decades"][decade_key]["summary"] = summary_data["summary"]
            timeline["decades"][decade_key]["key_achievements"] = summary_data["key_achievements"]

    # Enhance individual works
    for decade_key, decade_data in timeline["decades"].items():
        for category, works in decade_data.get("categories", {}).items():
            for work in works:
                title_lower = work.get("title", "").lower()
                for match_key, enhancement in work_enhancements.items():
                    if match_key in title_lower:
                        work["enhanced_description"] = enhancement["enhanced_description"]
                        work["related_themes"] = enhancement["related_themes"]
                        work["corpus_sources"] = ["dr-cortes-rag-corpus/extracted/blog_posts/"]
                        break

    return timeline

def main():
    print("Loading timeline data...")
    timeline = load_timeline()

    print("Creating enhanced biography...")
    timeline["biography"] = create_enhanced_biography()

    print("Creating decade summaries...")
    decade_summaries = create_decade_summaries()

    print("Creating work enhancements...")
    work_enhancements = enhance_work_descriptions()

    print("Applying enhancements...")
    timeline = apply_enhancements(timeline, decade_summaries, work_enhancements)

    print(f"Writing enhanced timeline to {OUTPUT_PATH}...")
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(timeline, f, indent=2, ensure_ascii=False)

    # Print summary
    print("\n=== Enhancement Summary ===")
    print(f"Biography: Added personal_background and {len(timeline['biography']['timeline_highlights'])} timeline highlights")

    for decade in timeline["decades"]:
        summary_len = len(timeline["decades"][decade].get("summary", ""))
        achievements = len(timeline["decades"][decade].get("key_achievements", []))
        print(f"{decade}: {summary_len} chars summary, {achievements} key achievements")

    enhanced_works = 0
    for decade_data in timeline["decades"].values():
        for works in decade_data.get("categories", {}).values():
            for work in works:
                if "enhanced_description" in work:
                    enhanced_works += 1

    print(f"\nWorks enhanced: {enhanced_works}")
    print(f"\nOutput saved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
