-- Script SQL pour ajouter les loyers différenciés au Monopoly
-- A exécuter sur la base de données 'monopoly'

-- Ajouter les colonnes pour les loyers différenciés si elles n'existent pas
ALTER TABLE proprietes 
ADD COLUMN IF NOT EXISTS loyer_1_maison INT DEFAULT NULL,
ADD COLUMN IF NOT EXISTS loyer_2_maisons INT DEFAULT NULL,
ADD COLUMN IF NOT EXISTS loyer_3_maisons INT DEFAULT NULL,
ADD COLUMN IF NOT EXISTS loyer_4_maisons INT DEFAULT NULL,
ADD COLUMN IF NOT EXISTS loyer_hotel INT DEFAULT NULL;

-- Mettre à jour les loyers différenciés pour les propriétés du Monopoly français
-- Quartier Marron
UPDATE proprietes SET 
    loyer_1_maison = 10, loyer_2_maisons = 30, loyer_3_maisons = 90, 
    loyer_4_maisons = 160, loyer_hotel = 250
WHERE nom = 'Boulevard de Belleville' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 20, loyer_2_maisons = 60, loyer_3_maisons = 180, 
    loyer_4_maisons = 320, loyer_hotel = 450
WHERE nom = 'Rue Lecourbe' AND type_propriete_code = 'propriete';

-- Quartier Bleu Clair
UPDATE proprietes SET 
    loyer_1_maison = 30, loyer_2_maisons = 90, loyer_3_maisons = 270, 
    loyer_4_maisons = 400, loyer_hotel = 550
WHERE nom = 'Rue de Vaugirard' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 30, loyer_2_maisons = 90, loyer_3_maisons = 270, 
    loyer_4_maisons = 400, loyer_hotel = 550
WHERE nom = 'Rue de Courcelles' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 40, loyer_2_maisons = 100, loyer_3_maisons = 300, 
    loyer_4_maisons = 450, loyer_hotel = 600
WHERE nom = 'Avenue de la République' AND type_propriete_code = 'propriete';

-- Quartier Rose
UPDATE proprietes SET 
    loyer_1_maison = 50, loyer_2_maisons = 150, loyer_3_maisons = 450, 
    loyer_4_maisons = 625, loyer_hotel = 750
WHERE nom = 'Boulevard de la Villette' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 50, loyer_2_maisons = 150, loyer_3_maisons = 450, 
    loyer_4_maisons = 625, loyer_hotel = 750
WHERE nom = 'Avenue de Neuilly' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 60, loyer_2_maisons = 180, loyer_3_maisons = 500, 
    loyer_4_maisons = 700, loyer_hotel = 900
WHERE nom = 'Rue de Paradis' AND type_propriete_code = 'propriete';

-- Quartier Orange
UPDATE proprietes SET 
    loyer_1_maison = 70, loyer_2_maisons = 200, loyer_3_maisons = 550, 
    loyer_4_maisons = 750, loyer_hotel = 950
WHERE nom = 'Avenue Mozart' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 70, loyer_2_maisons = 200, loyer_3_maisons = 550, 
    loyer_4_maisons = 750, loyer_hotel = 950
WHERE nom = 'Boulevard Saint-Michel' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 80, loyer_2_maisons = 220, loyer_3_maisons = 600, 
    loyer_4_maisons = 800, loyer_hotel = 1000
WHERE nom = 'Place Pigalle' AND type_propriete_code = 'propriete';

-- Quartier Rouge
UPDATE proprietes SET 
    loyer_1_maison = 90, loyer_2_maisons = 250, loyer_3_maisons = 700, 
    loyer_4_maisons = 875, loyer_hotel = 1050
WHERE nom = 'Avenue Matignon' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 90, loyer_2_maisons = 250, loyer_3_maisons = 700, 
    loyer_4_maisons = 875, loyer_hotel = 1050
WHERE nom = 'Boulevard Malesherbes' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 100, loyer_2_maisons = 300, loyer_3_maisons = 750, 
    loyer_4_maisons = 925, loyer_hotel = 1100
WHERE nom = 'Avenue Henri-Martin' AND type_propriete_code = 'propriete';

-- Quartier Jaune
UPDATE proprietes SET 
    loyer_1_maison = 110, loyer_2_maisons = 330, loyer_3_maisons = 800, 
    loyer_4_maisons = 975, loyer_hotel = 1150
WHERE nom = 'Faubourg Saint-Honoré' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 110, loyer_2_maisons = 330, loyer_3_maisons = 800, 
    loyer_4_maisons = 975, loyer_hotel = 1150
WHERE nom = 'Place de la Bourse' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 120, loyer_2_maisons = 360, loyer_3_maisons = 850, 
    loyer_4_maisons = 1025, loyer_hotel = 1200
WHERE nom = 'Rue La Fayette' AND type_propriete_code = 'propriete';

-- Quartier Vert
UPDATE proprietes SET 
    loyer_1_maison = 130, loyer_2_maisons = 390, loyer_3_maisons = 900, 
    loyer_4_maisons = 1100, loyer_hotel = 1275
WHERE nom = 'Avenue de Breteuil' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 130, loyer_2_maisons = 390, loyer_3_maisons = 900, 
    loyer_4_maisons = 1100, loyer_hotel = 1275
WHERE nom = 'Avenue Foch' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 150, loyer_2_maisons = 450, loyer_3_maisons = 1000, 
    loyer_4_maisons = 1200, loyer_hotel = 1400
WHERE nom = 'Boulevard des Capucines' AND type_propriete_code = 'propriete';

-- Quartier Bleu Foncé
UPDATE proprietes SET 
    loyer_1_maison = 175, loyer_2_maisons = 500, loyer_3_maisons = 1100, 
    loyer_4_maisons = 1300, loyer_hotel = 1500
WHERE nom = 'Avenue des Champs-Élysées' AND type_propriete_code = 'propriete';

UPDATE proprietes SET 
    loyer_1_maison = 200, loyer_2_maisons = 600, loyer_3_maisons = 1400, 
    loyer_4_maisons = 1700, loyer_hotel = 2000
WHERE nom = 'Rue de la Paix' AND type_propriete_code = 'propriete';

-- Mettre à jour la vue pour inclure les nouveaux loyers
CREATE OR REPLACE VIEW v_proprietes AS
SELECT 
    position,
    nom,
    type_propriete_code,
    prix_achat,
    loyer_base,
    loyer_1_maison,
    loyer_2_maisons,
    loyer_3_maisons,
    loyer_4_maisons,
    loyer_hotel,
    couleur,
    prix_maison
FROM proprietes;

-- Vérification des données
SELECT nom, loyer_base, loyer_1_maison, loyer_2_maisons, loyer_3_maisons, loyer_4_maisons, loyer_hotel
FROM proprietes
WHERE type_propriete_code = 'propriete'
ORDER BY position;
