import pydot

# Create a new graph
graph = pydot.Dot(graph_type='digraph')

# Define nodes for each table
tables = {
    "Client": ["id_client", "nom", "prenom"],
    "Bus": ["id_bus", "immatriculation", "nombre_places"],
    "Chauffeur": ["id_chauffeur", "nom", "prenom", "email"],
    "Trajet": ["id_trajet", "depart", "arrivee", "correspondance", "id_chauffeur", "id_administrateur"],
    "Administrateur": ["id_administrateur", "nom", "prenom", "email"],
    "Employe_service_de_maintenance": ["id_maintenance", "nom", "prenom", "email"],
    "Date": ["id_date", "jour", "heure"],
    "Ticket": ["id_ticket", "date_achat", "prix", "id_client"],
    "Reserver": ["id_client", "id_date", "id_bus"],
    "Entretenir": ["id_maintenance", "id_bus"]
}

# Add nodes to the graph
for table, columns in tables.items():
    label = f"{table}|" + "|".join(columns)
    node = pydot.Node(table, shape="record", label="{" + label + "}")
    graph.add_node(node)

# Define relationships (foreign keys)
relationships = [
    ("Trajet", "Chauffeur", "id_chauffeur"),
    ("Trajet", "Administrateur", "id_administrateur"),
    ("Reserver", "Client", "id_client"),
    ("Reserver", "Date", "id_date"),
    ("Reserver", "Bus", "id_bus"),
    ("Ticket", "Client", "id_client"),
    ("Entretenir", "Employe_service_de_maintenance", "id_maintenance"),
    ("Entretenir", "Bus", "id_bus")
]

# Add edges to the graph
for src, dst, col in relationships:
    edge = pydot.Edge(src, dst, label=col)
    graph.add_edge(edge)

# Save the graph to a file
graph.write_png("MLD.png")
