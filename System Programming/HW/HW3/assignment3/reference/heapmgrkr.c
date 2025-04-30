/*--------------------------------------------------------------------*/
/* heapmrgkr.c                                                        */
/* Author: Bob Dondero, nearly identical to code from the K&R book    */
/*--------------------------------------------------------------------*/

#include "heapmgr.h"

struct header {       /* block header */
   struct header *ptr; /* next block if on free list */
   unsigned size;     /* size of this block */
};

typedef struct header Header;

static Header base;       /* empty list to get started */
static Header *freep = NULL;     /* start of free list */

static Header *morecore(unsigned);

/* malloc:  general-purpose storage allocator */
void *heapmgr_malloc(size_t nbytes)
{
    Header *p, *prevp;
    unsigned nunits;

    nunits = (nbytes+sizeof(Header)-1)/sizeof(Header) + 1;
    if ((prevp = freep) == NULL) { /* no free list yet */
        base.ptr = freep = prevp = &base;
        base.size = 0;
    }
    for (p = prevp->ptr; ; prevp = p, p = p->ptr) {
        if (p->size >= nunits) {    /* big enough */
            if (p->size == nunits)     /* exactly */
                prevp->ptr = p->ptr;
            else {             /* allocate tail end */
                p->size -= nunits;
                p += p->size;
                p->size = nunits;
            }
            freep = prevp;
            return (void*)(p+1);
        }
        if (p == freep)  /* wrapped around free list */
            if ((p = morecore(nunits)) == NULL)
                return NULL;   /* none left */
    }
}

#define NALLOC 1024

/* morecore:  ask system for more memory */
static Header *morecore(unsigned int nu)
{
    char *cp, *sbrk(int);
    Header *up;

    if (nu < NALLOC)
        nu = NALLOC;
    cp = sbrk(nu * sizeof(Header));
    if (cp == (char *) -1)  /* no space at all */
        return NULL;
    up = (Header *) cp;
    up->size = nu;
    heapmgr_free((void *)(up+1));
    return freep;
}

/* free:  put block ap in free list */
void heapmgr_free(void *ap)
{
    Header *bp, *p;

    bp = (Header *)ap - 1;    /* point to block header */
    for (p = freep; !(bp > p && bp < p->ptr); p = p->ptr)
        if (p >= p->ptr && (bp > p || bp < p->ptr))
            break;  /* freed block at start or end of arena */

    if (bp + bp->size == p->ptr) {    /* join to upper nbr */
        bp->size += p->ptr->size;
        bp->ptr = p->ptr->ptr;
    } else
        bp->ptr = p->ptr;
    if (p + p->size == bp) {            /* join to lower nbr */
        p->size += bp->size;
        p->ptr = bp->ptr;
    } else
        p->ptr = bp;
    freep = p;
}