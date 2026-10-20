# Two-coffee-shop probability

## Question

Two drinks are sampled from each of two coffee shops. What is the probability
that both drinks from the first shop score higher than both drinks from the second?

State the statistical assumptions before calculating.

## Assumptions to examine

- Are all four scores drawn from the same distribution?
- Is the joint score model exchangeable across the four labeled drinks?
- Can scores tie?
- Are scores independent, or does sampling introduce dependence?

Independent, identically distributed scores from a continuous distribution are
one sufficient model. More generally, exchangeability with no ties is enough
for the rank-label argument below.

## Solution under the exchangeable, no-ties model

Rank all four drinks from highest to lowest. There are six equally likely ways
to place the two first-shop labels among the four ranked positions:

1. AABB
2. ABAB
3. ABBA
4. BAAB
5. BABA
6. BBAA

Only AABB has both first-shop drinks above both second-shop drinks. The
probability is therefore 1/6.

Equivalently, the number of label placements is "4 choose 2," which equals six.

## Extensions

- Change the event to either shop occupying both top ranks, rather than a
  specified shop. Which rank-label arrangements now qualify? Explain why this
  is a different event before calculating its probability.
- Explain why different shop-quality distributions can invalidate the equal-likelihood argument.
- Decide how ties affect the event "score higher" and calculate an example with discrete scores.
- Check the result with a seeded simulation under the stated model.
- Generalize to m drinks from the first shop and n from the second under the
  same exchangeable, no-ties model.

## Related exercises

- [Technical communication and validation](technical_communication.md) covers making assumptions explicit before presenting a result.
