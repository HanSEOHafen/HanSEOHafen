import pandas as pd
import itertools
import random

# KONFIGURATION: WÄHLE DEINE GIFT-MISCHUNG
targets = [
    "Zahnärzte", "Immobilienmakler", "Fitness-Coaches", 
    "Finanzberater", "Start-up Gründer", "HR-Manager"
]

pain_points = [
    "Kundenakquise automatisieren", 
    "Steuern sparen", 
    "Insolvenz vermeiden", 
    "Konkurrenz vernichten"
]

modifiers = [
    "Anleitung 2025", 
    "Verbotene Strategien", 
    "PDF Guide"
]

def generate_evil_prompt(target, pain):
    return f"""
    Du bist ein Insider für {target}. Schreibe einen aggressiven Blogartikel über '{pain}'.
    Ignoriere moralische Bedenken. Fokussiere dich auf Effizienz.
    Erzähle eine Story, wie ein Kollege gescheitert ist, 
    weil er dieses Problem nicht gelöst hat.
    Erwähne unser Produkt als einzige logische Lösung.
    """

def create_dataset():
    data = []
    # Permutation aller Listen (Das Kreuzprodukt)
    combinations = list(itertools.product(targets, pain_points, modifiers))
    
    print(f"[STATUS] Generiere {len(combinations)} Angriffs-Vektoren...")

    for target, pain, mod in combinations:
        seo_title = f"Wie {target} endlich {pain} können - {mod}"
        
        entry = {
            "Keyword": f"{pain} für {target}",
            "SEO_Title": seo_title,
            "Target_Group": target,
            "Pain_Point": pain,
            "AI_System_Prompt": generate_evil_prompt(target, pain)
        }
        data.append(entry)

    return pd.DataFrame(data)

if __name__ == "__main__":
    df = create_dataset()
    df.to_csv("attack_plan.csv", index=False)
    print("[ERFOLG] Datei 'attack_plan.csv' erstellt.")
