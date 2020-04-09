# Checkpoint

Checkpoint 는 모델이 사용한 매개변수를 저장해둔다. 이후 저장된 매개변수 값을 사용할 때 유용하다. 

텐서플로에서는 `tf.train.Chekpoint` 객체로 만들 수 있다.

```python
checkpoint_path = os.path.join(config.base_dir, 'checkpoints')
ckpt = tf.train.Checkpoint(encoder=encoder,
                           decoder=decoder,
                           optimizer = optimizer)
ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=3)
```

체크포인트를 생성하고, 저장할 변수들을 넣는다.

`CheckpointManager` 로 편리하게 관리할 수 있다.

`ckpt_manager.save()` 로 저장한다.

`max-keep` 은 몇개까지 유지할지를 설정한다.

```python
print(manager.checkpoints)
```

유지되고 있는 chcekpoint 를 확인할 수 있다.

```python
ckpt.restore(ckpt_manager.latest_checkpoint)
```

저장된 변수값을 불러온다.

