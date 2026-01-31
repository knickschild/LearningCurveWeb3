<!--
  <<< Author notes: Step 6 >>>
  This step introduces Clarity's map data structure.
  Maps are essential for storing key-value data in smart contracts.
  Link to Stacks/Clarity docs for further explanations.
-->

## Step 6: Understanding Clarity Maps

_Great progress on your Web3 learning journey! :rocket:_

This is a great introduction to Clarity's map data structure! Let's break this down and provide some context to help you fully understand what's happening.

### What Maps Are in Clarity

Maps in Clarity are key-value storage structures - think of them like a filing cabinet where each drawer has a label (key) and contains some information (value). They're persistent, meaning data stored in maps survives between contract calls.

### Breaking Down Your Example

**Map Definition:**

```clarity
(define-map balances principal uint)
```

This creates a map called "balances" where:

- Keys are `principal` types (wallet addresses)
- Values are `uint` types (unsigned integers)
- Think of it as: "Who has how much?"

**Setting Data:**

```clarity
(map-set balances tx-sender u500)
```

This stores the value `u500` (500) associated with the key `tx-sender` (whoever called this function). It's like saying "the person who sent this transaction now has a balance of 500."

**Retrieving Data:**

```clarity
(print (map-get? balances tx-sender))
```

This looks up the balance for `tx-sender`. Note the `?` - `map-get?` returns an optional type because the key might not exist.

### Complete Working Example

Here's a more comprehensive example that shows maps in action:

```clarity
;; Define a map to store user balances
(define-map balances principal uint)

;; Define a map to store user profiles with multiple fields
(define-map user-profiles
  principal
  { name: (string-ascii 50), level: uint, active: bool }
)

;; Function to set a user's balance
(define-public (set-balance (amount uint))
  (begin
    (map-set balances tx-sender amount)
    (ok amount)
  )
)

;; Function to get a user's balance
(define-read-only (get-balance (user principal))
  (default-to u0 (map-get? balances user))
)

;; Function to create a user profile
(define-public (create-profile (name (string-ascii 50)))
  (begin
    (map-set user-profiles tx-sender { name: name, level: u1, active: true })
    (ok true)
  )
)

;; Function to get a user's profile
(define-read-only (get-profile (user principal))
  (map-get? user-profiles user)
)
```

### Key Map Functions

| Function | Description | Returns |
|----------|-------------|---------|
| `map-set` | Sets or updates a value for a key | `bool` |
| `map-get?` | Retrieves a value by key | `(optional ...)` |
| `map-insert` | Inserts only if key doesn't exist | `bool` |
| `map-delete` | Removes a key-value pair | `bool` |

### :keyboard: Activity: Practice with Maps

1. Open the [Clarity Playground](https://clarity.tools/) in a new browser tab.
2. Create a simple map that stores a user's score.
3. Write a function to update the score.
4. Write a function to retrieve the score.
5. Test your contract by calling the functions.

### Important Notes

- **Maps are persistent**: Data stored in maps remains in the blockchain state.
- **Maps are not iterable**: You cannot loop through all entries in a map.
- **Keys must be unique**: Each key can only have one associated value.
- **Optional returns**: `map-get?` returns `none` if the key doesn't exist.

### Next Steps

Now that you understand maps, you're ready to build more complex smart contracts that can store and manage user data, token balances, and much more!
