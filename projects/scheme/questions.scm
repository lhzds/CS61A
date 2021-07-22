(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
    (define (cons-with first)
        (lambda (rest) (cons first rest)))
    (map (cons-with first) rests))

(define (zip pairs)
    (if (null? (car pairs))
        nil
        (cons
            (map car pairs)
            (zip (map cdr pairs))))
)

;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
    (define (enumerate-helper s idx)
        (if (null? s)
            nil
            (cons
                (list idx (car s))
                (enumerate-helper (cdr s) (+ idx 1)))))
    (enumerate-helper s 0)
  )
  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 17
    (cond
        ((= total 0)
            (list nil))
        ((or (null? denoms) (< total 0) (<= (car denoms) 0))
            nil)
        ((>= total (car denoms))
            (append 
                (cons-all
                    (car denoms)
                    (list-change 
                        (- total (car denoms))
                        denoms))
                (list-change
                    total
                    (cdr denoms))))
        (else (list-change
                total
                (cdr denoms))))
)
  ; END PROBLEM 17

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (cons form (cons params (let-to-lambda body)))
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (define zipped (zip values))
           (cons (cons 'lambda (cons (car zipped) (let-to-lambda body))) (let-to-lambda (cadr zipped)))
           ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18
         (map let-to-lambda expr)
         ; END PROBLEM 18
         )))