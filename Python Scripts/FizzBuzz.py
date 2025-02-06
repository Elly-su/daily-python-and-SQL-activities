from typing import List

def fizz_buzz_encode(x: int) -> List[int]:
    if x%15 == 0:
        return [0,0,0,1]
    elif x % 5 == 0:
        return [0,0,1,0]
    elif x % 3 == 0:
        return [0,1,0,0]
    else:
        return [1,0,0,0]
    assert fizz_buzz_encode(2) == [1,0,0,0]
    assert fizz_buzz_encode(6) == [0,1,0,0]
    assert fizz_buzz_encode(10) == [0,0,1,0]
    assert fizz_buzz_encode(30) == [0,0,0,1]
    def binary_encode(x: int) -> vector:
        binary: List[float] = []
        for i in range(10):
            binary.append(x % z)
            x = x // 2
            return binary
        xs = [binary_encode(n) for n in range(101,1024)]
        ys = [fizz_buzz_encode(n) for n in range(101,1024)]
        NUM_HIDDEN = 25
        #This is the hidden layer 10 inputs -> NUM_HIDDEN outputs
        network = [[random.random() for _ in range(10+1)] for _ in range(NUM_HIDDEN)]
        
        #This is the output layer NUM_HIDDEN inputs -> 4 outputs
        [[random.random() for _ in range(NUM_HIDDEN + 1)] for _ in range(4)]
        
        from scratch.linear_algebra import squared_distance
        learning_rate = 1.0
        with tqdm.trange(500) as t:
            for epoch in t:
                epoch_loss = 0.0
                for x,y in zip(xs,ys):
                    predicted = feed_forward(network,x)[-1]
                    epoch_loss += squared_distance(predicted,y)
                    gradients = sqerror_gradients(network,x,y)
                    network = [[gradient_step(neuron,grad,-learning_rate)]]
                    for neuron, grad in zip(layer, layer_grad):
                        for layer , layer_grad in zip(network, gradients):
                            t.set_description(f"fizz buzz (loss: (epoch_loss:2f))")
                            
                            def argmax(xs: list) -> int:
                                return max(range(len(xs)), key = lambda i: xs[i])
                            assert argmax([0, -1]) == 0
                            assert argmax([-1, 0]) == 1
                            assert argmax([-1, 10, 5, 20, -3]) == 3
                            
                            num_correct = 0
                            for n in range (1, 101):
                                x = binary_encode(n)
                                predicted = argmax(feed_forward(network,x)[-1]) 
                                actual = argmax(fizz_buzz_encode(n))
                                labels = [str(n), "fizz", "buzz", "fizzbuzz"]
                                print(n, labels[predicted], labels[actual])
                                if predicted == actual:
                                    num_correct += 1
                                    print(num_correct, "/", 100)
                    
                    
                    
                    
                    
                    
                    
        
        
        
        