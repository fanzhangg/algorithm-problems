## The Biggest Game of the Year
 
Playoff season is over and the game we’ve all been waiting for is coming up! It’s the ultimate sport–the Puppy Bowl, in which fearsome puppies fight for the ultimate prize... or just pee on the field. (Yes, this is a real event, and yes, they play it non-stop on repeat at my vet’s office). You have been asked by the organizers of the Puppy Bowl to help get the puppies organized before the filming. In particular (because the herders are always trying to herd the retrievers, who are always trying to retrieve the toy breeds, who are always tripping the herders), they want the puppies sorted by into three types: herders, retrievers and toy breeds. When you arrive at the filming studio, you see that n puppies, which each belong to one of the three types, are randomly arranged in a line of exactly n kennels (there are no extra kennels). You are able to look into one kennel at a time and determine what type the dog is, and you are only able to swap the kennels of two dogs at a time (otherwise you would have a hairy mess). You want to rearrange the dogs in the kennels so that all the herders come first, then the retrievers and finally the toy breeds.

More formally, you are given an array A[1...n] of n dogs. Each dog A[i] has a type: t(A[i]) ∈ (herd,retr,toy). Rearrange array A so that all items of type herd come first, then all items of type retr, and then all items of type toy. The only operations allowed on this array are:
(a) for a particular i, you can query t(A[i])
(b) for two indices i and j, you can swap A[i] and A[j].

In particular, you cannot copy elements into an auxiliary array (as there are no extra kennels). Give an algorithm that runs in O(n) time.
Describe the algorithm and justify that it is correct and runs in O(n) (once again, this can be somewhat informal).