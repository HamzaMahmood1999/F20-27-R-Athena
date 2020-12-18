# F20-27-R-Athena

Final Year Project for FAST-NUCES.

Approach 4.1 and 4.2 are code based and have been sufficently expressed in their seperate folders

For Approach 4.3 you will need to install Protege (https://protege.stanford.edu/) and GraphDB Free (https://graphdb.ontotext.com/). Furthermore you will need to install the ACE view plugin for protege (http://attempto.ifi.uzh.ch/aceview/#6.2)

1. You will need to use the sentence extraction methods from Approach 4.1 to obtain senences (you can skip this part if your dataset already follows the "ACE ontology rules")
2. You will then copy/paste the sentences into the "ACE Text" View and press Update. This will convert the sentences into an ontology
3. Export the ontology in the "RDF/XML" format
4. Open GraphDB and make new Repository there.
5. Upload the exported file from Protege
6. Now you can view the visual graph or run SPARQL queries to test the file
