-- Script de création de la base de données Monopoly
-- Avec loyers différenciés

-- ============================================
-- Nettoyage
-- ============================================
DROP TABLE IF EXISTS proprietes;
DROP TABLE IF EXISTS types_proprietes;
DROP VIEW IF EXISTS v_proprietes;

-- ============================================
-- Table des types de propriétés
-- ============================================
CREATE TABLE IF NOT EXISTS types_proprietes (
    id INTEGER PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
    libelle VARCHAR(100) NOT NULL
);

INSERT INTO types_proprietes (id, code, libelle) VALUES
(1, 'propriete', 'Propriété'),
(2, 'gare', 'Gare'),
(3, 'compagnie', 'Compagnie');

-- ============================================
-- Table des propriétés avec loyers différenciés
-- ============================================
CREATE TABLE IF NOT EXISTS proprietes (
    position INTEGER PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    type_propriete_id INTEGER NOT NULL,
    prix_achat INTEGER,
    loyer_base INTEGER,
    loyer_1_maison INTEGER,
    loyer_2_maisons INTEGER,
    loyer_3_maisons INTEGER,
    loyer_4_maisons INTEGER,
    loyer_hotel INTEGER,
    couleur VARCHAR(50),
    prix_maison INTEGER,
    FOREIGN KEY (type_propriete_id) REFERENCES types_proprietes(id)
);

-- ============================================
-- Propriétés du plateau français
-- ============================================

-- Quartier Marron (2 propriétés)
INSERT INTO proprietes VALUES
(1, 'Boulevard de Belleville', 1, 60, 2, 10, 30, 90, 160, 250, 'marron', 50),
(3, 'Rue Lecourbe', 1, 60, 4, 20, 60, 180, 320, 450, 'marron', 50);

-- Gare Montparnasse
INSERT INTO proprietes VALUES
(5, 'Gare Montparnasse', 2, 200, 25, NULL, NULL, NULL, NULL, NULL, 'gare', 0);

-- Quartier Bleu Clair (3 propriétés)
INSERT INTO proprietes VALUES
(6, 'Rue de Vaugirard', 1, 100, 6, 30, 90, 270, 400, 550, 'bleu_clair', 50),
(8, 'Rue de Courcelles', 1, 100, 6, 30, 90, 270, 400, 550, 'bleu_clair', 50),
(9, 'Avenue de la République', 1, 120, 8, 40, 100, 300, 450, 600, 'bleu_clair', 50);

-- Quartier Rose (3 propriétés)
INSERT INTO proprietes VALUES
(11, 'Boulevard de la Villette', 1, 140, 10, 50, 150, 450, 625, 750, 'rose', 100),
(13, 'Avenue de Neuilly', 1, 140, 10, 50, 150, 450, 625, 750, 'rose', 100),
(14, 'Rue de Paradis', 1, 160, 12, 60, 180, 500, 700, 900, 'rose', 100);

-- Compagnie d'Électricité
INSERT INTO proprietes VALUES
(12, 'Compagnie d''Électricité', 3, 150, 0, NULL, NULL, NULL, NULL, NULL, 'compagnie', 0);

-- Gare de Lyon
INSERT INTO proprietes VALUES
(15, 'Gare de Lyon', 2, 200, 25, NULL, NULL, NULL, NULL, NULL, 'gare', 0);

-- Quartier Orange (3 propriétés)
INSERT INTO proprietes VALUES
(16, 'Avenue Mozart', 1, 180, 14, 70, 200, 550, 750, 950, 'orange', 100),
(18, 'Boulevard Saint-Michel', 1, 180, 14, 70, 200, 550, 750, 950, 'orange', 100),
(19, 'Place Pigalle', 1, 200, 16, 80, 220, 600, 800, 1000, 'orange', 100);

-- Quartier Rouge (3 propriétés)
INSERT INTO proprietes VALUES
(21, 'Avenue Matignon', 1, 220, 18, 90, 250, 700, 875, 1050, 'rouge', 150),
(23, 'Boulevard Malesherbes', 1, 220, 18, 90, 250, 700, 875, 1050, 'rouge', 150),
(24, 'Avenue Henri-Martin', 1, 240, 20, 100, 300, 750, 925, 1100, 'rouge', 150);

-- Gare du Nord
INSERT INTO proprietes VALUES
(25, 'Gare du Nord', 2, 200, 25, NULL, NULL, NULL, NULL, NULL, 'gare', 0);

-- Quartier Jaune (3 propriétés)
INSERT INTO proprietes VALUES
(26, 'Faubourg Saint-Honoré', 1, 260, 22, 110, 330, 800, 975, 1150, 'jaune', 150),
(27, 'Place de la Bourse', 1, 260, 22, 110, 330, 800, 975, 1150, 'jaune', 150),
(29, 'Rue La Fayette', 1, 280, 24, 120, 360, 850, 1025, 1200, 'jaune', 150);

-- Compagnie des Eaux
INSERT INTO proprietes VALUES
(28, 'Compagnie des Eaux', 3, 150, 0, NULL, NULL, NULL, NULL, NULL, 'compagnie', 0);

-- Quartier Vert (3 propriétés)
INSERT INTO proprietes VALUES
(31, 'Avenue de Breteuil', 1, 300, 26, 130, 390, 900, 1100, 1275, 'vert', 200),
(32, 'Avenue Foch', 1, 300, 26, 130, 390, 900, 1100, 1275, 'vert', 200),
(34, 'Boulevard des Capucines', 1, 320, 28, 150, 450, 1000, 1200, 1400, 'vert', 200);

-- Gare Saint-Lazare
INSERT INTO proprietes VALUES
(35, 'Gare Saint-Lazare', 2, 200, 25, NULL, NULL, NULL, NULL, NULL, 'gare', 0);

-- Quartier Bleu Foncé (2 propriétés)
INSERT INTO proprietes VALUES
(37, 'Avenue des Champs-Élysées', 1, 350, 35, 175, 500, 1100, 1300, 1500, 'bleu_fonce', 200),
(39, 'Rue de la Paix', 1, 400, 50, 200, 600, 1400, 1700, 2000, 'bleu_fonce', 200);

-- ============================================
-- Vue pour faciliter les requêtes
-- ============================================
CREATE VIEW v_proprietes AS
SELECT 
    p.position,
    p.nom,
    t.code AS type_propriete_code,
    t.libelle AS type_propriete_libelle,
    p.prix_achat,
    p.loyer_base,
    p.loyer_1_maison,
    p.loyer_2_maisons,
    p.loyer_3_maisons,
    p.loyer_4_maisons,
    p.loyer_hotel,
    p.couleur,
    p.prix_maison
FROM proprietes p
JOIN types_proprietes t ON p.type_propriete_id = t.id
ORDER BY p.position;
