from pathlib import Path

for name in ('index.html', 'redesign.py', 'styles.css'):
    path = Path(name)
    text = path.read_text(encoding='utf-8')
    text = text.replace('findili-art', 'recommendation-art')
    text = text.replace('>findili<span', '>neural<span')
    text = text.replace('<h3>Findili</h3>', '<h3>Système de recommandation par réseau de neurones</h3>')
    text = text.replace('<span>STARTUP</span>', '<span>RECOMMANDATION</span>')
    text = text.replace('Un réseau de neurones profond pour associer chaque utilisateur aux missions qui lui correspondent.', 'Un système de recommandation fondé sur un réseau de neurones profond pour proposer des correspondances personnalisées.')
    text = text.replace('m<span>mission</span>', 'r<span>recommandation</span>')
    text = text.replace('À la recherche d’un développeur au Nouveau-Brunswick ?<br>J’aimerais en savoir plus sur votre projet.', 'Basé à Moncton, au Canada, et prêt à déménager pour travailler.<br>Discutons de vos projets, où que vous soyez.')
    text = text.replace('Je transforme des problèmes complexes en solutions concrètes. Du premier pixel au dernier algorithme.', 'Je transforme des problèmes complexes en solutions concrètes. Basé à Moncton, au Canada, je suis mobile pour de nouvelles opportunités.')
    text = text.replace('Moncton, Canada.\">', 'Moncton, Canada. Mobile pour travailler.\">')
    path.write_text(text, encoding='utf-8')

print('Contenu, styles et générateur mis à jour.')
