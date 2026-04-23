def assess_graph_approach_suitability(problem_description):
    """
    Assess whether a problem might benefit from graph-based approaches.

    Args:
        problem_description (dict): Dictionary containing problem characteristics.

    Returns:
        tuple:
            score (float): Suitability score (0 to 1)
            explanation (str): Recommendation with explanation
    """

    # Factors favoring graph approaches
    graph_factors = {
        'relationship_importance': 'Relationships between entities are crucial',
        'interconnected_data': 'Data points influence each other',
        'network_effects': 'Network effects or propagation are present',
        'structural_patterns': 'Structural patterns are relevant',
        'variable_neighborhoods': 'Entities have variable numbers of connections',
        'non_euclidean': 'Data exists in non-Euclidean space'
    }

    # Count present factors
    present_factors = 0

    for factor in graph_factors:
        if problem_description.get(factor, False):
            present_factors += 1

    # Score calculation
    score = present_factors / len(graph_factors)

    # Recommendation based on score
    if score > 0.7:
        recommendation = "Graph-based approach highly recommended"
    elif score > 0.3:
        recommendation = "Consider graph-based approach alongside traditional methods"
    else:
        recommendation = "Traditional tabular methods may be sufficient"

    # Explanation generation
    present_factor_desc = []

    for factor, desc in graph_factors.items():
        if problem_description.get(factor, False):
            present_factor_desc.append(desc)

    if present_factor_desc:
        explanation = "Factors favoring graph approach: " + "; ".join(present_factor_desc)
    else:
        explanation = "No strong factors favoring graph approach"

    return score, recommendation + ". " + explanation


# ---------------------------
# Example Problems
# ---------------------------

fraud_detection = {
    'relationship_importance': True,
    'interconnected_data': True,
    'network_effects': True,
    'structural_patterns': True,
    'variable_neighborhoods': True,
    'non_euclidean': True
}

simple_classification = {
    'relationship_importance': False,
    'interconnected_data': False,
    'network_effects': False,
    'structural_patterns': False,
    'variable_neighborhoods': False,
    'non_euclidean': False
}

recommendation_system = {
    'relationship_importance': True,
    'interconnected_data': True,
    'network_effects': True,
    'structural_patterns': False,
    'variable_neighborhoods': True,
    'non_euclidean': False
}

social_network_analysis = {
    'relationship_importance': True,
    'interconnected_data': True,
    'network_effects': True,
    'structural_patterns': True,
    'variable_neighborhoods': True,
    'non_euclidean': True
}

# ---------------------------
# Testing All Examples
# ---------------------------

problems = {
    "Fraud Detection Problem": fraud_detection,
    "Simple Classification Problem": simple_classification,
    "Recommendation System Problem": recommendation_system,
    "Social Network Analysis Problem": social_network_analysis
}

for problem_name, problem_data in problems.items():
    print("=" * 60)
    print(problem_name)
    score, explanation = assess_graph_approach_suitability(problem_data)
    print("Score:", round(score, 2))
    print("Result:", explanation)
    print()
