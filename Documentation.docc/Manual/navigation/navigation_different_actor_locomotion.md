# Support different actor locomotion

@Image(source: "nav_actor_locomotion.png")

To support different actor locomotion like crouching and crawling, a similar
map setup as supporting <doc:navigation_different_actor_types> is required.

Bake different navigation meshes with an appropriate height for crouched
or crawling actors so they can find paths through those narrow sections in your game world.

When an actor changes locomotion state, e.g. stands up, starts
crouching or crawling, query the appropriate map for a path.

If the avoidance behavior should also change with the locomotion e.g. only avoid while standing or only avoid
other agents in the same locomotion state, switch the actor's avoidance agent to another avoidance map with each locomotion change.

> Note:
>
> While a path query can be execute immediately for multiple maps, the avoidance agent map switch will only take effect after the next server synchronization.