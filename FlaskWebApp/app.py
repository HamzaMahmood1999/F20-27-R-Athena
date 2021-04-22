from flask import Flask, redirect, url_for, render_template, request
import os

#os.system("pip install --upgrade neuralcoref")
#os.system("pip install urllib3")
# os.system("pip uninstall --yes spacy")
# os.system("pip install --upgrade spacy==2.1.0")
#import neuralcoref
import spacy

from bs4 import BeautifulSoup
import requests
import re
import csv
import pickle
from py2neo import Graph
from py2neo import Node, Relationship
import pandas as pd
import numpy as np
import spacy

app=Flask(__name__, template_folder='templates')




@app.route('/')
def home():
    return render_template("index.html")

@app.route("/home", methods=["POST", "GET"])
def homepage():
    return render_template("homepage.html")

@app.route("/text", methods=["POST", "GET"])
def text():
    if request.method == "GET":
        return render_template("textarea.html")

    else:
        text = request.form["rawtext"]
        print(text)
        return redirect(url_for("testroute"))


@app.route("/test",  methods=["POST", "GET"])
def testroute():
    return render_template("newgraph.html")

@app.route("/showgraph", methods=["POST", "GET"])
def graphviz():
    return render_template("grpahviz.html")



@app.route("/newgraph", methods=["POST", "GET"])
def model():
    # os.system("pip uninstall --yes spacy")
    # os.system("pip install --upgrade spacy==2.1.0")
    #
    # #os.system("python -m spacy download en_core_web_sm")
    #
    # #Co-refrencing
    # # Load SpaCy
    # nlp = spacy.load('en_core_web_sm')
    # # Add neural coref to SpaCy's pipe
    # neuralcoref.add_to_pipe(nlp)
    # doc = nlp(text)
    # # fetches tokens with whitespaces from spacy document
    # tok_list = list(token.text_with_ws for token in doc)
    # for cluster in doc._.coref_clusters:
    #     # get tokens from representative cluster name
    #     cluster_main_words = set(cluster.main.text.split(' '))
    #     for coref in cluster:
    #         if coref != cluster.main:  # if coreference element is not the representative element of that cluster
    #             if coref.text != cluster.main.text and bool(
    #                     set(coref.text.split(' ')).intersection(cluster_main_words)) == False:
    #                 # if coreference element text and representative element text are not equal and none of the coreference element words are in representative element. This was done to handle nested coreference scenarios
    #                 tok_list[coref.start] = cluster.main.text + \
    #                                         doc[coref.end - 1].whitespace_
    #                 for i in range(coref.start + 1, coref.end):
    #                     tok_list[i] = ""
    #
    #
    # os.system("pip install textacy")
    # os.system("pip install --upgrade spacy")
    import textacy
    # from textacy.extract import subject_verb_object_triples
    # #SVO generation
    # data_dir = ''
    # TEXTS = [app.open_resource("static/Preprocessed_hbl.txt").read()]
    # nlp = spacy.load('en_core_web_sm')
    # final_svos = []
    # final_text_svos = []
    # entity_dict = {}
    # svo_labels = []
    # for i, text in enumerate(TEXTS):
    #     doc = nlp(text)
    #     for ent in doc.ents:
    #         if ent not in entity_dict.keys():
    #             entity_dict[str(ent)] = ent.label_
    #             # print(ent.label)
    #     svos = list(subject_verb_object_triples(doc))
    #     # print(svos, "/n")
    #     # svos = subject_verb_object_triples(doc)
    #     svos_text = [(str(x[0]).strip(), str(x[1]).strip(), str(x[2]).strip()) for x in svos]
    #     print(svos_text)
    #     final_svos = final_svos + svos
    #     final_text_svos = final_text_svos + svos_text
    #
    # for svo in final_text_svos:
    #     tup = ['Object', 'Object']
    #     if (svo[0] in entity_dict.keys()):
    #         tup[0] = entity_dict[svo[0]]
    #
    #     if (svo[2] in entity_dict.keys()):
    #         tup[1] = entity_dict[svo[2]]
    #     svo_labels.append(tuple(tup))
    #
    # with open('svos.csv', 'w') as csvFile:
    #     writer = csv.writer(csvFile)
    #     writer.writerows(final_text_svos)
    # csvFile.close()
    #
    # df = pd.read_csv(r'svos.csv', header=None)
    # dataset = df.to_numpy()
    #
    # i = 0
    # j = 0
    # l1 = list()
    #
    # for i in range(0, len(dataset)):
    #     l2 = list()
    #     for j in range(0, len(dataset[j])):
    #         x = dataset[i][j].replace('[', '')
    #         y = x.replace(']', '')
    #         z = y.replace(',', '')
    #         l2.append(z)
    #     l1.append(l2)
    #
    # with open('output_svos.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(l1)
    #
    # with open('entity_dict.pickle', 'wb') as handle:
    #     pickle.dump(entity_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    #
    # #connecting to Neo4j
    #
    # svos = pd.read_csv("output_svos.csv", names=['sub', 'rel', 'obj'])
    # pickle_in = open("entity_dict.pickle", "rb")
    # entities = pickle.load(pickle_in)
    #
    # # Connect to Neo4j using corresponding <port:7687> and <password>
    #
    # graph = Graph("bolt://localhost:7687", auth=("neo4j", "24601"))
    #
    # graph.delete_all()
    #
    # # Parse the entities and build the knowledge graph in Neo4j Database
    # for index, row in svos.iterrows():
    #     sub, rel, obj = row
    #     sub_node = graph.nodes.match(entities.get(sub, "Object"), name=sub).first()
    #     obj_node = graph.nodes.match("Object", name=obj).first()
    #     if not sub_node:
    #         sub_node = Node(entities.get(sub, "Object"), name=sub)
    #     if not obj_node:
    #         obj_node = Node(entities.get(obj, "Object"), name=obj)
    #     relation = Relationship.type(rel)
    #     graph.merge(relation(sub_node, obj_node), entities.get(sub, "Object"), "name")

    return render_template("newgraph.html")

if __name__ == '__main__':
    app.run(debug=True)
