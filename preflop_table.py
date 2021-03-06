#-------------------------------------------------------------------------------
# Name:        preflop_table.py
# Purpose:     Store deterministic winning probabilities in preflop stage.
#-------------------------------------------------------------------------------

import numpy as np


# The probabilities used for first bet.
table_1=np.asarray([[	0.852	,	0.67	,	0.662	,	0.654	,	0.646	,	0.628	,	0.619	,	0.61	,	0.599	,	0.599	,	0.595	,	0.582	,	0.574	]	,
[	0.653	,	0.824	,	0.634	,	0.626	,	0.618	,	0.6	,	0.583	,	0.575	,	0.566	,	0.558	,	0.549	,	0.541	,	0.532	]	,
[	0.644	,	0.614	,	0.799	,	0.602	,	0.595	,	0.577	,	0.56	,	0.543	,	0.536	,	0.528	,	0.519	,	0.51	,	0.502	]	,
[	0.636	,	0.606	,	0.581	,	0.775	,	0.575	,	0.557	,	0.54	,	0.523	,	0.506	,	0.5	,	0.491	,	0.482	,	0.474	]	,
[	0.627	,	0.597	,	0.572	,	0.552	,	0.75	,	0.54	,	0.523	,	0.506	,	0.489	,	0.472	,	0.465	,	0.457	,	0.448	]	,
[	0.608	,	0.578	,	0.554	,	0.532	,	0.515	,	0.72	,	0.508	,	0.491	,	0.474	,	0.457	,	0.439	,	0.433	,	0.424	]	,
[	0.599	,	0.56	,	0.536	,	0.515	,	0.497	,	0.481	,	0.692	,	0.479	,	0.432	,	0.445	,	0.427	,	0.409	,	0.403	]	,
[	0.588	,	0.552	,	0.518	,	0.497	,	0.479	,	0.433	,	0.45	,	0.662	,	0.454	,	0.437	,	0.418	,	0.4	,	0.382	]	,
[	0.577	,	0.542	,	0.51	,	0.478	,	0.431	,	0.445	,	0.432	,	0.423	,	0.633	,	0.431	,	0.413	,	0.395	,	0.377	]	,
[	0.577	,	0.533	,	0.501	,	0.472	,	0.442	,	0.427	,	0.414	,	0.405	,	0.399	,	0.603	,	0.414	,	0.397	,	0.378	]	,
[	0.567	,	0.523	,	0.491	,	0.462	,	0.435	,	0.407	,	0.394	,	0.385	,	0.38	,	0.382	,	0.567	,	0.386	,	0.368	]	,
[	0.558	,	0.514	,	0.482	,	0.453	,	0.426	,	0.4	,	0.375	,	0.366	,	0.361	,	0.363	,	0.351	,	0.537	,	0.36	]	,
[	0.549	,	0.505	,	0.473	,	0.443	,	0.417	,	0.391	,	0.368	,	0.346	,	0.341	,	0.343	,	0.332	,	0.323	,	0.503	]	])

# The probabilities used for second bet. (bet after another player's bet)
table_2=np.asarray([[	0.869	,	0.634	,	0.603	,	0.571	,	0.539	,	0.498	,	0.468	,	0.439	,	0.412	,	0.407	,	0.392	,	0.382	,	0.371	]	,
[	0.616	,	0.717	,	0.43	,	0.426	,	0.423	,	0.403	,	0.356	,	0.386	,	0.381	,	0.372	,	0.364	,	0.356	,	0.348	]	,
[	0.583	,	0.4	,	0.694	,	0.432	,	0.429	,	0.409	,	0.395	,	0.379	,	0.377	,	0.369	,	0.361	,	0.353	,	0.344	]	,
[	0.549	,	0.39	,	0.4	,	0.671	,	0.435	,	0.416	,	0.401	,	0.386	,	0.37	,	0.365	,	0.357	,	0.349	,	0.341	]	,
[	0.515	,	0.391	,	0.4	,	0.404	,	0.648	,	0.422	,	0.408	,	0.392	,	0.377	,	0.359	,	0.353	,	0.345	,	0.337	]	,
[	0.471	,	0.37	,	0.376	,	0.383	,	0.39	,	0.618	,	0.41	,	0.395	,	0.381	,	0.362	,	0.344	,	0.339	,	0.331	]	,
[	0.439	,	0.354	,	0.361	,	0.368	,	0.375	,	0.377	,	0.594	,	0.401	,	0.387	,	0.368	,	0.35	,	0.331	,	0.326	]	,
[	0.408	,	0.351	,	0.344	,	0.351	,	0.358	,	0.362	,	0.368	,	0.568	,	0.391	,	0.372	,	0.354	,	0.335	,	0.317	]	,
[	0.379	,	0.346	,	0.342	,	0.335	,	0.342	,	0.346	,	0.353	,	0.357	,	0.543	,	0.378	,	0.36	,	0.335	,	0.316	]	,
[	0.373	,	0.336	,	0.333	,	0.329	,	0.323	,	0.326	,	0.333	,	0.337	,	0.344	,	0.519	,	0.365	,	0.341	,	0.322	]	,
[	0.357	,	0.328	,	0.324	,	0.321	,	0.317	,	0.307	,	0.313	,	0.318	,	0.324	,	0.33	,	0.489	,	0.347	,	0.319	]	,
[	0.346	,	0.319	,	0.316	,	0.312	,	0.308	,	0.301	,	0.293	,	0.298	,	0.304	,	0.311	,	0.301	,	0.459	,	0.31	]	,
[	0.335	,	0.311	,	0.307	,	0.303	,	0.3	,	0.292	,	0.288	,	0.278	,	0.284	,	0.29	,	0.281	,	0.271	,	0.429	]	]
)

# The probabilities used for third bet. (bet again that another player has bet after yourself)
table_3=np.asarray([[	0.852	,	0.61	,	0.572	,	0.537	,	0.501	,	0.457	,	0.427	,	0.401	,	0.385	,	0.389	,	0.38	,	0.371	,	0.363	]	,
[	0.59	,	0.726	,	0.435	,	0.424	,	0.413	,	0.39	,	0.375	,	0.37	,	0.372	,	0.366	,	0.359	,	0.351	,	0.344	]	,
[	0.551	,	0.405	,	0.69	,	0.414	,	0.41	,	0.391	,	0.376	,	0.359	,	0.364	,	0.357	,	0.35	,	0.343	,	0.335	]	,
[	0.512	,	0.392	,	0.386	,	0.657	,	0.414	,	0.395	,	0.38	,	0.363	,	0.355	,	0.351	,	0.344	,	0.337	,	0.329	]	,
[	0.474	,	0.38	,	0.378	,	0.382	,	0.624	,	0.4	,	0.382	,	0.369	,	0.36	,	0.344	,	0.339	,	0.332	,	0.324	]	,
[	0.427	,	0.356	,	0.358	,	0.362	,	0.368	,	0.587	,	0.388	,	0.373	,	0.364	,	0.348	,	0.33	,	0.326	,	0.318	]	,
[	0.395	,	0.34	,	0.341	,	0.346	,	0.352	,	0.355	,	0.558	,	0.377	,	0.369	,	0.353	,	0.335	,	0.317	,	0.312	]	,
[	0.367	,	0.336	,	0.324	,	0.329	,	0.335	,	0.339	,	0.344	,	0.527	,	0.372	,	0.356	,	0.338	,	0.321	,	0.303	]	,
[	0.35	,	0.337	,	0.328	,	0.319	,	0.325	,	0.33	,	0.335	,	0.339	,	0.503	,	0.367	,	0.349	,	0.332	,	0.314	]	,
[	0.354	,	0.33	,	0.322	,	0.316	,	0.308	,	0.312	,	0.318	,	0.322	,	0.333	,	0.481	,	0.356	,	0.339	,	0.321	]	,
[	0.344	,	0.323	,	0.314	,	0.308	,	0.303	,	0.294	,	0.299	,	0.303	,	0.314	,	0.322	,	0.455	,	0.331	,	0.313	]	,
[	0.335	,	0.315	,	0.306	,	0.3	,	0.295	,	0.289	,	0.28	,	0.284	,	0.296	,	0.303	,	0.295	,	0.43	,	0.304	]	,
[	0.326	,	0.307	,	0.298	,	0.292	,	0.287	,	0.281	,	0.275	,	0.265	,	0.277	,	0.284	,	0.276	,	0.267	,	0.405	]	]
)

# card index from string to int
cards_index={'A':0,'K':1,'Q':2,'J':3,'T':4,'9':5,'8':6,'7':7,'6':8,'5':9,'4':10,'3':11,'2':12}


# Query the probability table above.
def card_prob(input_card1,input_card2,table_index):
    '''
    input_card1, input_card2: two hole cards.
    table_index: which table to use.
    return: the probability.
    '''
    card_ind1=cards_index[input_card1[0]]
    card_ind2=cards_index[input_card2[0]]

    if card_ind1>card_ind2:
        card_ind_high=card_ind1
        card_ind_low=card_ind2
    else:
        card_ind_high=card_ind2
        card_ind_low=card_ind1

    if table_index==1:
        pre_flot_table=table_1
    elif table_index==2:
        pre_flot_table=table_2
    else:
        pre_flot_table=table_3

    if input_card1[1]==input_card2[1]:
        return pre_flot_table[card_ind_low][card_ind_high]
    else:
        return pre_flot_table[card_ind_high][card_ind_low]

